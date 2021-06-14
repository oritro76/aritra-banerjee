import pytest

from data.data_gen import DataGenerator


@pytest.fixture
def return_random_product():
    data_gen = DataGenerator()
    return data_gen.create_product()


@pytest.fixture
def return_random_store():
    data_gen = DataGenerator()
    return data_gen.create_store()


@pytest.fixture
def return_random_service():
    data_gen = DataGenerator()
    return data_gen.create_service()

@pytest.fixture
def return_random_category():
    data_gen = DataGenerator()
    return data_gen.create_category()
