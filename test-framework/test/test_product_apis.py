import pytest
from jsonschema import validate
from assertpy import assert_that

from clients.api_playground_client import ApiPlaygroundClient
from response_json_schema.api_schema import *


@pytest.mark.smoketest
def test_create_product_api_returns_201_with_valid_json_schema(return_random_product):
    client = ApiPlaygroundClient()
    product = return_random_product
    res = client.create_product(product)
    assert_that(res['status_code']).is_equal_to(201)
    validate(res['json'], response_create_product)


@pytest.mark.endtoendtest
def test_create_product_api_returns_400_when_required_fields_are_missing():
    client = ApiPlaygroundClient()
    product = {}
    res = client.create_product(product)
    assert_that(res['status_code']).is_equal_to(400)
    assert_that(len(res['json']['errors'])).is_equal_to(len(response_create_product['required']))
    validate(res['json'], response_error_400)


@pytest.mark.endtoendtest
def test_create_product_api_returns_400_when_price_is_in_wrong_format(return_random_product):
    client = ApiPlaygroundClient()
    product = return_random_product
    product['price'] = 100.111
    res = client.create_product(product)
    assert_that(res['status_code']).is_equal_to(400)
    assert_that(res['json']['errors'][0]).is_equal_to("'price' should be multiple of 0.01")
    validate(res['json'], response_error_400)


@pytest.mark.smoketest
def test_fetch_product_api_with_product_id_return_200_with_valid_json_schema(return_random_product):
    client = ApiPlaygroundClient()
    product = return_random_product
    res = client.create_product(product)

    assert_that(res['status_code']).is_equal_to(201)

    prd_id = res['json']['id']
    res = client.fetch_products(prd_id=prd_id)

    assert_that(res['status_code']).is_equal_to(200)
    validate(res['json'], response_create_product)


@pytest.mark.endtoendtest
def test_fetch_product_api_return_404_for_invalid_product_id(return_random_product):
    client = ApiPlaygroundClient()
    res = client.fetch_products(prd_id=1234123412341234)

    assert_that(res['status_code']).is_equal_to(404)


@pytest.mark.endtoendtest
def test_edit_product_api_return_200_with_valid_json_schema(return_random_product):
    client = ApiPlaygroundClient()
    product = return_random_product

    res = client.create_product(product)

    assert_that(res['status_code']).is_equal_to(201)

    changed_name = 'edited product'
    product['name'] = changed_name

    prd_id = res['json']['id']
    res = client.edit_product(prd_id=prd_id, product=product)

    assert_that(res['status_code']).is_equal_to(200)
    validate(res['json'], response_create_product)
    assert_that(res['json']['name']).is_equal_to(changed_name)


@pytest.mark.endtoendtest
def test_delete_product_api_return_200_with_valid_json_schema(return_random_product):
    client = ApiPlaygroundClient()
    product = return_random_product

    res = client.create_product(product)

    assert_that(res['status_code']).is_equal_to(201)

    prd_id = res['json']['id']
    res = client.delete_product(prd_id=prd_id)

    assert_that(res['status_code']).is_equal_to(200)
    validate(res['json'], response_create_product)

    res = client.fetch_products(prd_id=prd_id)

    assert_that(res['status_code']).is_equal_to(404)


@pytest.mark.smoketest
def test_fetch_products_api_returns_200_with_valid_json_schema():
    client = ApiPlaygroundClient()
    res = client.fetch_products()
    assert_that(res['status_code']).is_equal_to(200)
    assert_that(res['json']['limit']).is_equal_to(10)
    assert_that(res['json']['skip']).is_equal_to(0)
    validate(res['json'], response_fetch_products)


@pytest.mark.endtoendtest
def test_fetch_products_api_allows_pagination():
    client = ApiPlaygroundClient()

    params = {
        '$limit': 15,
        '$skip': 15
    }

    res = client.fetch_products(params=params)
    assert_that(res['status_code']).is_equal_to(200)
    assert_that(int(res['json']['limit'])).is_equal_to(15)
    assert_that(int(res['json']['skip'])).is_equal_to(15)
    validate(res['json'], response_fetch_products)


@pytest.mark.endtoendtest
def test_fetch_product_api_returns_products_based_on_partial_product_names():
    client = ApiPlaygroundClient()

    params = {
        'name[$like]': '*TV*',
    }

    res = client.fetch_products(params=params)
    assert_that(res['status_code']).is_equal_to(200)
    assert_that(len(res['json']['data'])).is_greater_than(0)
    validate(res['json'], response_fetch_products)


@pytest.mark.endtoendtest
def test_fetch_product_api_returns_products_based_on_category_names():
    client = ApiPlaygroundClient()

    params = {
        'category.name': 'TVs',
    }

    res = client.fetch_products(params=params)
    assert_that(res['status_code']).is_equal_to(200)
    assert_that(len(res['json']['data'])).is_greater_than(0)
    validate(res['json'], response_fetch_products)


@pytest.mark.endtoendtest
def test_fetch_product_api_returns_products_based_on_category_id():
    client = ApiPlaygroundClient()

    params = {
        'category.id': 'abcat0101000',
    }

    res = client.fetch_products(params=params)
    assert_that(res['status_code']).is_equal_to(200)
    assert_that(len(res['json']['data'])).is_greater_than(0)
    validate(res['json'], response_fetch_products)


@pytest.mark.endtoendtest
def test_fetch_product_api_returns_sorted_products_based_on_price():
    client = ApiPlaygroundClient()

    params = {
        '$sort[price]': '-1',
        'category.name': 'TVs',
    }

    res = client.fetch_products(params=params)
    assert_that(res['status_code']).is_equal_to(200)
    assert_that(len(res['json']['data'])).is_greater_than(0)
    assert_that(res['json']['data'][0]['price']).is_greater_than(res['json']['data'][9]['price'])
    validate(res['json'], response_fetch_products)


@pytest.mark.endtoendtest
def test_fetch_product_api_returns_selected_properties_only():
    client = ApiPlaygroundClient()

    params = {
        '$select[]': 'name',
    }

    res = client.fetch_products(params=params)
    assert_that(res['status_code']).is_equal_to(200)

    product = res['json']['data'][0]

    assert_that('name' in product).is_true()
    assert_that('price' in product).is_false()
    validate(res['json'], response_fetch_products)
