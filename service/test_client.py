from .base_api_client import BaseAPIClient
from .endpoints.member_endpoint import MemberEndpoint
from .endpoints.cucumber_endpoint import CucumberEndpoint


if __name__ == "__main__":
    client = BaseAPIClient()


member_api = CucumberEndpoint()
response = member_api.retrieve_person(50)
print(response)
