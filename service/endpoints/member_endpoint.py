from service.base_api_client import BaseTASAPIClient
from utils.url_utils import generate_base_url


class MemberEndpoint(BaseTASAPIClient):
    def __init__(self):
        super().__init__()
        self.base_url = generate_base_url()

    TAS_V1_MEMBERS = 'v1/members'
    TAS_V1_MEMBERS_ID = 'v1/members/%s'

    def get_member_by_id(self, member_id):
        endpoint = self.TAS_V1_MEMBERS_ID % member_id
        return self.get(endpoint)

# Usage example:
# member_api = MemberEndpoint()
# member_data = member_api.get_member_by_id(123)
# print(member_data)
