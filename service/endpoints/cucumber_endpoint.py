from service.base_api_client import BaseAPIClient
from utils.logger.logger_util import setup_logger

LOGGER = setup_logger(__name__)


class CucumberEndpoint(BaseAPIClient):
    def __init__(self):
        super().__init__()

    TAS_V1_CUCUMBER_OBJECT_MEMBER = 'v1/cucumber/object/member'
    TAS_V1_CUCUMBER_OBJECT_PERSON = 'v1/cucumber/object/person'
    TAS_V1_CUCUMBER_GENERATOR_ADMIN = 'generator/admin'
    TAS_V1_CUCUMBER_GENERATOR_MEMBER = 'generator/member'
    TAS_V1_CUCUMBER_OBJECT_GROUP = 'object/group'

    def retrieve_person(self, args, expected_code=200):
        LOGGER.info(f"Retrieving TAS person with expected code {expected_code}")
        payload = {'attributes': args}
        return self.get_with_payload(self.TAS_V1_CUCUMBER_OBJECT_PERSON, payload, expected_code)
