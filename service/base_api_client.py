import requests
from utils.url_utils import generate_base_url
import json
import time
from utils.logger.logger_util import setup_logger

LOGGER = setup_logger(__name__)


class BaseAPIClient:
    def __init__(self):
        self.base_url = generate_base_url(service_type='api')
        self.token = self.authenticate()
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

    def authenticate(self):
        auth_endpoint = "v1/authentication/login"
        auth_url = f"{self.base_url}{auth_endpoint}"  # Use the base_url attribute here
        params = {
            "username": 'sadmin',
            "password": 'test1234',
            "domain": "Admin"
        }
        headers = {
            "Teladoc-api-request-token": "c32dabe321dc0b42b418c42b17fcc42c7932f363"
        }
        response = requests.get(auth_url, headers=headers, params=params)
        if response.status_code != 200:
            raise Exception("Authentication request failed!")

        response_data = response.json()
        token = response_data['auth_token']
        print(f"Authentication Token: {token}")
        return token

    def get(self, endpoint, params=None, pp=False):
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, headers=self.headers, params=params)
        if response.status_code != 200:
            raise Exception(f"GET request to {url} failed with status code {response.status_code}!")

        data = response.json()

        if pp:
            print(json.dumps(data, indent=4))

        return data

    def set_authorization_header(self, type, token):
        self.headers['Authorization'] = f"{type} {token}"

    def get_with_payload(self, path, payload, expected_code, params=None, additional_headers=None, parse_response=True,
                         timeout=10):
        # Ensure that there's no leading slash in the path to avoid double slashes
        path = path.lstrip('/')

        # Construct the URL
        url = f"{self.base_url}{path}"

        # Convert payload to JSON
        json_payload = json.dumps(payload)

        # Log the endpoint and payload
        LOGGER.info(f"Sending GET request to {url}")
        LOGGER.info(f"Payload: {json_payload}")
        if params:
            LOGGER.info(f"Parameters: {params}")

        # Merge additional headers if provided
        headers = self.headers
        if additional_headers:
            headers.update(additional_headers)

        # Initialize response before the loop
        response = None

        # Use a loop to retry the request until the timeout
        elapsed_time = 0
        polling_interval = 2
        while elapsed_time < timeout:
            response = requests.get(url, headers=headers, params=params, data=json_payload)

            # Validate response code
            if response.status_code == expected_code:
                break
            else:
                time.sleep(polling_interval)
                elapsed_time += polling_interval

        # Raise an exception if the response code doesn't match the expected code after retries
        if not response or response.status_code != expected_code:
            raise Exception(
                f"GET request to {url} failed with status code {response.status_code if response else 'None'}. Expected {expected_code}!")

        # Parse the response if required
        if parse_response:
            return response.json()
        else:
            return response
