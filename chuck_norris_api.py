import requests

BASE_URL = "https://api.chucknorris.io/jokes"

def get_random_joke():
    response = requests.get(f"{BASE_URL}/random")
    data = response.json()
    return data["value"]

def get_categories():
    response = requests.get(f"{BASE_URL}/categories")
    data = response.json()
    return data

def get_random_joke_from_category(category):
    response = requests.get(f"{BASE_URL}/random?category={category}")
    data = response.json()
    return data["value"]

def get_jokes_count_in_category(category):
    response = requests.get(f"{BASE_URL}/search?query=all&category={category}")
    data = response.json()
    return data["total"]
