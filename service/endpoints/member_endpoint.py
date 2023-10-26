from ..base_api_client import BaseAPIClient
from utils.url_utils import generate_base_url


class MemberEndpoint(BaseAPIClient):
    def __init__(self):
        super().__init__()
        self.base_url = "https://tas.oshuk-759-1.uat.teladoc.io/"

    TAS_V1_MEMBERS_ID = 'v1/members/%s'

    def retrieve_member_by_id(self, member_id):
        endpoint = self.TAS_V1_MEMBERS_ID % member_id
        return self.get(endpoint)
