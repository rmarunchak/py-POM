import requests
import os
from utils.url_utils import generate_base_url
import json
import time
from requests.exceptions import RequestException, HTTPError, Timeout, ConnectionError


class BaseAPIClient:
    def __init__(self):
        self.base_url = generate_base_url(service_type='api')
        self.token = None
        self.headers = {
            'Content-Type': 'application/json'
        }

    def authenticate(self, username, password):
        auth_endpoint = "v1/authentication/login"
        auth_url = f"{self.base_url}{auth_endpoint}"
        payload = {
            "username": username,
            "password": password,
            "domain": "Admin"
        }
        response = requests.post(auth_url, json=payload)
        if response.status_code == 200:
            self.token = response.json().get('auth_token')
            self.headers['Authorization'] = f"Bearer {self.token}"
            self.headers['set-cookie'] = f"auth_token={self.token}"
        else:
            raise Exception("Authentication failed!")

    # Read
    def get(self, endpoint, params=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, headers=self.headers, params=params)
        if not self.handle_response(response):
            response = requests.get(url, headers=self.headers, params=params)
        return response.json()

    # Create
    def post(self, endpoint, data=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.post(url, headers=self.headers, json=data)
        if not self.handle_response(response):
            response = requests.post(url, headers=self.headers, json=data)
        return response.json()

    # Update
    def put(self, endpoint, data=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.put(url, headers=self.headers, json=data)
        if not self.handle_response(response):
            response = requests.put(url, headers=self.headers, json=data)
        return response.json()

    # Delete
    def delete(self, endpoint, params=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.delete(url, headers=self.headers, params=params)
        if not self.handle_response(response):
            response = requests.delete(url, headers=self.headers, params=params)
        return response.json()

    def handle_response(self, response):
        if 'Invalid access token' in str(response.content):
            self.authenticate(os.environ.get('TAS_API_SUPER_ADMIN_USERNAME'),
                              os.environ.get('TAS_API_SUPER_ADMIN_PASSWORD'))
            return False
        return True

    def get_with_payload(self, path, payload, expected_code, params=None, additional_headers=None, parse_response=True,
                         timeout=10):
        end_time = time.time() + timeout
        response = None

        while time.time() < end_time:
            try:
                # Convert payload to JSON
                payload_json = json.dumps(payload)

                # Merge headers if additional headers are provided
                headers = self.headers
                if additional_headers:
                    headers.update(additional_headers)

                response = self.get(path, params=params)
                # Validate response code
                self.validate_response_code(response, expected_code)
                break
            except (RequestException, HTTPError, Timeout, ConnectionError) as e:
                # Log the exception for debugging purposes
                print(f"Error occurred: {e}")
                # Wait for 2 seconds before retrying
                time.sleep(2)

        # Parse response if required
        if parse_response:
            return response.json()
        else:
            return response

    @staticmethod
    def validate_response_code(response, expected_code):
        if response.status_code != expected_code:
            raise Exception(f"Expected status code {expected_code}, but got {response.status_code}")
