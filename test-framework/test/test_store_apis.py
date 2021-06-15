import pytest
from jsonschema import validate
from assertpy import assert_that

from clients.api_playground_client import ApiPlaygroundClient
from response_json_schema.api_schema import *


@pytest.mark.smoketest
def test_create_store_api_returns_201_with_valid_json_schema(return_random_store):
    client = ApiPlaygroundClient()
    store = return_random_store

    res = client.create_store(store)
    assert_that(res['status_code']).is_equal_to(201)
    validate(res['json'], response_create_store)


@pytest.mark.endtoendtest
def test_create_store_api_returns_400_when_required_fields_are_missing():
    client = ApiPlaygroundClient()
    store = {}
    res = client.create_store(store)
    assert_that(res['status_code']).is_equal_to(400)
    assert_that(len(res['json']['errors'])).is_equal_to(len(response_create_store['required']))
    validate(res['json'], response_error_400)


@pytest.mark.endtoendtest
def test_fetch_store_api_with_store_id_return_200_with_valid_json_schema(return_random_store):
    client = ApiPlaygroundClient()
    store = return_random_store

    res = client.create_store(store)

    assert_that(res['status_code']).is_equal_to(201)

    str_id = res['json']['id']
    res = client.fetch_stores(str_id=str_id)

    assert_that(res['status_code']).is_equal_to(200)
    validate(res['json'], response_create_store)


@pytest.mark.endtoendtest
def test_fetch_store_api_return_404_for_invalid_store_id():
    client = ApiPlaygroundClient()
    res = client.fetch_stores(str_id=1234123412341234)

    assert_that(res['status_code']).is_equal_to(404)


@pytest.mark.endtoendtest
def test_edit_store_api_return_200_with_valid_json_schema(return_random_store):
    client = ApiPlaygroundClient()
    store = return_random_store

    res = client.create_store(store)
    assert_that(res['status_code']).is_equal_to(201)

    changed_name = "edited store"
    store['name'] = changed_name

    str_id = res['json']['id']
    res = client.edit_store(str_id=str_id, store=store)

    assert_that(res['status_code']).is_equal_to(200)
    validate(res['json'], response_create_store)
    assert_that(res['json']['name']).is_equal_to(changed_name)


@pytest.mark.endtoendtest
def test_delete_store_api_return_200_with_valid_json_schema(return_random_store):
    client = ApiPlaygroundClient()
    store = return_random_store

    res = client.create_store(store)
    assert_that(res['status_code']).is_equal_to(201)

    str_id = res['json']['id']
    res = client.delete_store(str_id=str_id)

    assert_that(res['status_code']).is_equal_to(200)
    validate(res['json'], response_create_store)

    res = client.fetch_stores(str_id=str_id)
    assert_that(res['status_code']).is_equal_to(404)


@pytest.mark.smoketest
def test_fetch_stores_api_returns_200_with_valid_json_schema():
    client = ApiPlaygroundClient()

    res = client.fetch_stores()
    assert_that(res['status_code']).is_equal_to(200)
    validate(res['json'], response_fetch_stores)
    assert_that(res['json']['limit']).is_equal_to(10)
    assert_that(res['json']['skip']).is_equal_to(0)


@pytest.mark.endtoendtest
def test_fetch_store_api_allows_pagination():
    client = ApiPlaygroundClient()

    params = {
        '$limit': 15,
        '$skip': 15
    }

    res = client.fetch_stores(params=params)
    assert_that(res['status_code']).is_equal_to(200)
    assert_that(int(res['json']['limit'])).is_equal_to(15)
    assert_that(int(res['json']['skip'])).is_equal_to(15)
    validate(res['json'], response_fetch_stores)


@pytest.mark.endtoendtest
def test_fetch_store_api_returns_stores_based_on_partial_store_names():
    client = ApiPlaygroundClient()

    params = {
        'name[$like]': '*Richfield*',
    }

    res = client.fetch_stores(params=params)
    assert_that(res['status_code']).is_equal_to(200)
    assert_that(len(res['json']['data'])).is_greater_than(0)
    validate(res['json'], response_fetch_stores)


@pytest.mark.endtoendtest
def test_fetch_store_api_returns_stores_nearby():
    client = ApiPlaygroundClient()

    params = {
        'near': '90210',
    }

    res = client.fetch_stores(params=params)
    assert_that(res['status_code']).is_equal_to(200)
    assert_that(len(res['json']['data'])).is_greater_than(0)
    assert_that(res['json']['data'][0]['city']).is_equal_to('Los Angeles')
    validate(res['json'], response_fetch_stores)


@pytest.mark.endtoendtest
def test_fetch_store_api_returns_stores_based_on_offered_services():
    client = ApiPlaygroundClient()

    params = {
        'service[name]': 'Best Buy Mobile',
    }

    res = client.fetch_stores(params=params)
    assert_that(res['status_code']).is_equal_to(200)
    assert_that(len(res['json']['data'])).is_greater_than(0)
    validate(res['json'], response_fetch_stores)


@pytest.mark.endtoendtest
def test_fetch_store_api_returns_selected_properties_only():
    client = ApiPlaygroundClient()

    params = {
        '$select[]': 'name',
    }

    res = client.fetch_stores(params=params)
    assert_that(res['status_code']).is_equal_to(200)

    store = res['json']['data'][0]

    assert_that('name' in store).is_true()
    assert_that('price' in store).is_false()
    validate(res['json'], response_fetch_stores)
