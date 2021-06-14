import pytest
from jsonschema import validate
from assertpy import assert_that

from conf.conf import api_version
from clients.api_playground_client import ApiPlaygroundClient
from response_json_schema.api_schema import *


@pytest.mark.smoketest
def test_fetch_api_version_returns_correct_api_version_with_valid_json_schema():
    client = ApiPlaygroundClient()
    res = client.fetch_api_version()
    assert_that(res['status_code']).is_equal_to(200)
    validate(res['json'], response_fetch_api_version)
    version = res['json']['version']
    assert_that(version).is_equal_to(api_version)


@pytest.mark.smoketest
def test_health_check_returns_200():
    client = ApiPlaygroundClient()
    res = client.health_check()
    assert_that(res['status_code']).is_equal_to(200)





















