import pytest
from jsonschema import validate
from assertpy import assert_that

from clients.api_playground_client import ApiPlaygroundClient
from response_json_schema.api_schema import *


@pytest.mark.endtoendtest
@pytest.mark.smoketest
def test_create_service_api_returns_201_with_valid_json_schema(return_random_service):
    client = ApiPlaygroundClient()
    service = return_random_service

    res = client.create_service(service)
    assert_that(res['status_code']).is_equal_to(201)
    validate(res['json'], response_create_service)


@pytest.mark.endtoendtest
def test_create_service_api_returns_400_when_required_fields_are_missing():
    client = ApiPlaygroundClient()
    service = {}
    res = client.create_service(service)
    assert_that(res['status_code']).is_equal_to(400)
    assert_that(len(res['json']['errors'])).is_equal_to(len(response_create_service['required']))
    validate(res['json'], response_error_400)


@pytest.mark.endtoendtest
def test_fetch_service_api_with_service_id_return_200_with_valid_json_schema(return_random_service):
    client = ApiPlaygroundClient()
    service = return_random_service

    res = client.create_service(service)
    assert_that(res['status_code']).is_equal_to(201)

    srv_id = res['json']['id']
    res = client.fetch_services(srv_id=srv_id)

    assert_that(res['status_code']).is_equal_to(200)
    validate(res['json'], response_create_service)


@pytest.mark.endtoendtest
def test_edit_service_api_return_200_with_valid_json_schema(return_random_service):
    client = ApiPlaygroundClient()
    service = return_random_service

    res = client.create_service(service)
    assert_that(res['status_code']).is_equal_to(201)

    changed_name = "edited service"
    service['name'] = changed_name

    srv_id = res['json']['id']
    res = client.edit_service(srv_id=srv_id, service=service)

    assert_that(res['status_code']).is_equal_to(200)
    validate(res['json'], response_create_service)
    assert_that(res['json']['name']).is_equal_to(changed_name)


@pytest.mark.endtoendtest
def test_fetch_service_api_return_404_for_invalid_service_id():
    client = ApiPlaygroundClient()
    res = client.fetch_services(srv_id=1234123412341234)

    assert_that(res['status_code']).is_equal_to(404)


@pytest.mark.endtoendtest
def test_delete_service_api_return_200_with_valid_json_schema(return_random_service):
    client = ApiPlaygroundClient()
    service = return_random_service

    res = client.create_service(service)
    assert_that(res['status_code']).is_equal_to(201)

    srv_id = res['json']['id']
    res = client.delete_service(srv_id=srv_id)

    assert_that(res['status_code']).is_equal_to(200)
    validate(res['json'], response_create_service)

    res = client.fetch_services(srv_id=srv_id)
    assert_that(res['status_code']).is_equal_to(404)


@pytest.mark.endtoendtest
@pytest.mark.smoketest
def test_fetch_services_api_returns_200_with_valid_json_schema():
    client = ApiPlaygroundClient()

    res = client.fetch_services()
    assert_that(res['status_code']).is_equal_to(200)
    validate(res['json'], response_fetch_stores)
    assert_that(res['json']['limit']).is_equal_to(10)
    assert_that(res['json']['skip']).is_equal_to(0)


@pytest.mark.endtoendtest
def test_fetch_services_api_allows_pagination():
    client = ApiPlaygroundClient()

    params = {
        '$limit': 15,
        '$skip': 15
    }

    res = client.fetch_services(params=params)
    assert_that(res['status_code']).is_equal_to(200)
    assert_that(int(res['json']['limit'])).is_equal_to(15)
    assert_that(int(res['json']['skip'])).is_equal_to(15)
    validate(res['json'], response_fetch_services)