from typing import Any
from utils.logger.logger_util import setup_logger

LOGGER = setup_logger(__name__)


class BaseAssert:
    @staticmethod
    def verify_object_equals(expected: Any, actual: Any, verified_attribute: str):
        LOGGER.info(f"Verifying \"{verified_attribute}\" object: [{expected}] equaling actual: [{actual}]")
        assert expected == actual, f"\"{verified_attribute}\" should be \"{expected}\", but \"{actual}\""

    @staticmethod
    def verify_object_contains(expected: str, actual: str, verified_attribute: str):
        LOGGER.info(f"Verifying \"{verified_attribute}\" object: [{actual}] contains expected: [{expected}]")
        assert expected.lower() in actual.lower(), f"\"{verified_attribute}\" \"{actual}\" should contains \"{expected}\", but not"

    @staticmethod
    def verify_object_not_contains(expected: str, actual: str, verified_attribute: str):
        LOGGER.info(f"Verifying \"{verified_attribute}\" object: [{actual}] does not contain expected: [{expected}]")
        assert expected.lower() not in actual.lower(), f"\"{verified_attribute}\" \"{actual}\" should not contain \"{expected}\", but it does"

    @staticmethod
    def verify_list_equals(expected: list, actual: list, verified_attribute: str):
        LOGGER.info(f"Verifying \"{verified_attribute}\" list: [{expected}] equaling actual: [{actual}]")
        assert expected == actual, f"\"{verified_attribute}\" list should be \"{expected}\", but \"{actual}\""

    @staticmethod
    def verify_list_contains(expected: list, actual: list, verified_attribute: str):
        LOGGER.info(f"Verifying \"{verified_attribute}\" list: [{actual}] contains expected: [{expected}]")
        for item in expected:
            assert item in actual, f"\"{verified_attribute}\" list \"{actual}\" should contain \"{item}\", but not"

    @staticmethod
    def verify_list_not_contains(expected: list, actual: list, verified_attribute: str):
        LOGGER.info(f"Verifying \"{verified_attribute}\" list: [{actual}] does not contain expected: [{expected}]")
        for item in expected:
            assert item not in actual, f"\"{verified_attribute}\" list \"{actual}\" should not contain \"{item}\", but it does"
