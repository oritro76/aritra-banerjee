import pytest
from jsonschema import validate
from assertpy import assert_that

from clients.api_playground_client import ApiPlaygroundClient
from response_json_schema.api_schema import *


@pytest.mark.smoketest
def test_create_category_api_returns_201_with_valid_json_schema(return_random_category):
    client = ApiPlaygroundClient()
    category = return_random_category

    res = client.create_category(category)
    assert_that(res['status_code']).is_equal_to(201)
    validate(res['json'], response_create_category)


@pytest.mark.endtoendtest
def test_create_category_api_returns_400_when_required_fields_are_missing():
    client = ApiPlaygroundClient()
    category = {}
    res = client.create_category(category)
    assert_that(res['status_code']).is_equal_to(400)
    assert_that(len(res['json']['errors'])).is_equal_to(len(response_create_category['required']))
    validate(res['json'], response_error_400)


@pytest.mark.endtoendtest
def test_fetch_category_api_with_category_id_return_200_with_valid_json_schema(return_random_category):
    client = ApiPlaygroundClient()
    category = return_random_category

    res = client.create_category(category)
    assert_that(res['status_code']).is_equal_to(201)

    cat_id = res['json']['id']
    res = client.fetch_categories(cat_id=cat_id)

    assert_that(res['status_code']).is_equal_to(200)
    validate(res['json'], response_create_category)


@pytest.mark.endtoendtest
def test_fetch_category_api_return_404_for_invalid_category_id():
    client = ApiPlaygroundClient()
    res = client.fetch_categories(cat_id=1234123412341234)

    assert_that(res['status_code']).is_equal_to(404)


@pytest.mark.endtoendtest
def test_edit_category_api_return_200_with_valid_json_schema(return_random_category):
    client = ApiPlaygroundClient()
    category = return_random_category

    res = client.create_category(category)
    assert_that(res['status_code']).is_equal_to(201)

    changed_name = "edited category"
    category['name'] = changed_name

    cat_id = res['json']['id']
    res = client.edit_category(cat_id=cat_id, category=category)

    assert_that(res['status_code']).is_equal_to(200)
    validate(res['json'], response_create_category)
    assert_that(res['json']['name']).is_equal_to(changed_name)


@pytest.mark.endtoendtest
def test_delete_category_api_return_200_with_valid_json_schema(return_random_category):
    client = ApiPlaygroundClient()
    category = return_random_category

    res = client.create_category(category)
    assert_that(res['status_code']).is_equal_to(201)

    cat_id = res['json']['id']
    res = client.delete_category(cat_id=cat_id)

    assert_that(res['status_code']).is_equal_to(200)
    validate(res['json'], response_create_category)

    res = client.fetch_categories(cat_id=cat_id)
    assert_that(res['status_code']).is_equal_to(404)


@pytest.mark.smoketest
def test_fetch_categories_api_returns_200_with_valid_json_schema():
    client = ApiPlaygroundClient()

    res = client.fetch_categories()
    assert_that(res['status_code']).is_equal_to(200)
    assert_that(res['json']['limit']).is_equal_to(10)
    assert_that(res['json']['skip']).is_equal_to(0)
    validate(res['json'], response_fetch_categories)


@pytest.mark.endtoendtest
def test_fetch_categories_api_allows_pagination():
    client = ApiPlaygroundClient()

    params = {
        '$limit': 15,
        '$skip': 15
    }

    res = client.fetch_categories(params=params)
    assert_that(res['status_code']).is_equal_to(200)
    assert_that(int(res['json']['limit'])).is_equal_to(15)
    assert_that(int(res['json']['skip'])).is_equal_to(15)
    validate(res['json'], response_fetch_categories)
