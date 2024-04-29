import pytest
import requests
from chuck_norris_api import *

BASE_URL = "https://api.chucknorris.io/jokes"

@pytest.mark.parametrize("func", [
    get_random_joke,
    lambda: get_random_joke_from_category(get_categories()[0]),
    lambda: get_random_joke_from_category(get_categories()[1]),
    lambda: get_random_joke_from_category(get_categories()[2]),
    lambda: get_random_joke_from_category(get_categories()[3]),
    lambda: get_random_joke_from_category(get_categories()[4]),
    lambda: get_random_joke_from_category(get_categories()[5]),
])
def test_joke_functions(func):
    joke = func()

    assert isinstance(joke, str)
    assert len(joke) > 0


@pytest.mark.parametrize("category", get_categories())
def test_get_jokes_count_in_category(category):
    count = get_jokes_count_in_category(category)

    assert isinstance(count, int)
    assert count > 0

@pytest.mark.parametrize("func, invalid_key", [
    (get_random_joke, "invalid_key"),
    (lambda: get_random_joke_from_category("invalid_category"), "invalid_key")
])
def test_invalid_response_key_error(func, invalid_key):
    with pytest.raises(KeyError):
        response = requests.get(f"{BASE_URL}/random")
        data = response.json()
        data[invalid_key]
