import requests
import os
from utils.url_utils import generate_base_url

class BaseTASAPIClient:
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
