from .base_api_client import BaseAPIClient
from .endpoints.member_endpoint import MemberEndpoint


if __name__ == "__main__":
    client = BaseAPIClient()


member_api = MemberEndpoint()
response = member_api.retrieve_member_by_id(50)
print(response)
