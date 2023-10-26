import requests
from utils.url_utils import generate_base_url


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

    def get(self, endpoint, params=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, headers=self.headers, params=params)
        if response.status_code != 200:
            raise Exception(f"GET request to {url} failed with status code {response.status_code}!")
        return response.json()

    def set_authorization_header(self, type, token):
        self.headers['Authorization'] = f"{type} {token}"
