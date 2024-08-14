import pytest


@pytest.fixture(scope="function", autouse=True)
def url():
    return "https://www.fatsecret.com"
