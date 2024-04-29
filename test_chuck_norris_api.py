import pytest
import requests
from chuck_norris_api import *

BASE_URL = "https://api.chucknorris.io/jokes"

def test_get_random_joke():
    joke = get_random_joke()

    assert isinstance(joke, str)
    assert len(joke) > 0

def test_get_categories():
    categories = get_categories()

    assert isinstance(categories, list)
    assert len(categories) > 0

def test_get_random_joke_from_category():
    categories = get_categories()
    category = categories[0]

    joke = get_random_joke_from_category(category)

    assert isinstance(joke, str)
    assert len(joke) > 0

def test_get_jokes_count_in_category():
    categories = get_categories()
    category = categories[0]

    count = get_jokes_count_in_category(category)

    assert isinstance(count, int)
    assert count > 0

def test_get_random_joke_invalid_response():
    with pytest.raises(KeyError) as exc_info:
        response = requests.get(f"{BASE_URL}/random")
        data = response.json()
        data["invalid_key"]
    
    assert "invalid_key" in str(exc_info.value)

def test_get_random_joke_from_category_invalid_response():
    with pytest.raises(KeyError):
        response = requests.get(f"{BASE_URL}/random?category=invalid_category")
        data = response.json()
        data["invalid_key"]

def test_get_jokes_count_in_category_invalid_response():
    with pytest.raises(KeyError):
        response = requests.get(f"{BASE_URL}/search?query=all&category=invalid_category")
        data = response.json()
        data["invalid_key"]