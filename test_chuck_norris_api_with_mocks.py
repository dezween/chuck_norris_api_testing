import pytest
import requests
from unittest.mock import patch
from chuck_norris_api import *

BASE_URL = "https://api.chucknorris.io/jokes"

def test_get_random_joke():
    with patch('requests.get') as mock_get:
        mock_response = {"value": "Random joke"}
        mock_get.return_value.json.return_value = mock_response

        joke = get_random_joke()

        assert joke == "Random joke"
        mock_get.assert_called_with(f"{BASE_URL}/random")

def test_get_categories():
    with patch('requests.get') as mock_get:
        mock_response = ["category1", "category2"]
        mock_get.return_value.json.return_value = mock_response

        categories = get_categories()

        assert categories == ["category1", "category2"]
        mock_get.assert_called_with(f"{BASE_URL}/categories")

def test_get_random_joke_from_category():
    with patch('requests.get') as mock_get:
        mock_response = {"value": "Random joke from category"}
        mock_get.return_value.json.return_value = mock_response

        joke = get_random_joke_from_category("category1")

        assert joke == "Random joke from category"
        mock_get.assert_called_with(f"{BASE_URL}/random?category=category1")

def test_get_jokes_count_in_category():
    with patch('requests.get') as mock_get:
        mock_response = {"total": 10}
        mock_get.return_value.json.return_value = mock_response

        count = get_jokes_count_in_category("category1")

        assert count == 10
        mock_get.assert_called_with(f"{BASE_URL}/search?query=all&category=category1")

def test_get_random_joke_invalid_response():
    with patch('requests.get') as mock_get:
        mock_response = {}
        mock_get.return_value.json.return_value = mock_response

        with pytest.raises(KeyError) as exc_info:
            get_random_joke()

        assert "value" in str(exc_info.value)

def test_get_random_joke_from_category_invalid_response():
    with patch('requests.get') as mock_get:
        mock_response = {}
        mock_get.return_value.json.return_value = mock_response

        with pytest.raises(KeyError):
            get_random_joke_from_category("category1")

def test_get_jokes_count_in_category_invalid_response():
    with patch('requests.get') as mock_get:
        mock_response = {}
        mock_get.return_value.json.return_value = mock_response

        with pytest.raises(KeyError):
            get_jokes_count_in_category("category1")