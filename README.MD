This project provides a Python module for interacting with the Chuck Norris API (https://api.chucknorris.io/). It allows
you to retrieve random jokes, get joke categories, fetch jokes from specific categories, and get the count of jokes in a
category.

## Files

- `chuck_norris_api.py`: Contains the main functions for interacting with the Chuck Norris API.
- `test_chuck_norris_api.py`: Contains unit tests for the functions in `chuck_norris_api.py` using the `pytest`
framework.
- `test_chuck_norris_api_with_mocks.py`: Contains unit tests for the functions in `chuck_norris_api.py` using the
`pytest` framework and mocking the API responses with the `unittest.mock` module.
- `test_chuck_norris_api_with_parametrize.py`: Contains parametrized unit tests for the functions in
`chuck_norris_api.py` using the `pytest` framework and the `@pytest.mark.parametrize` decorator.

## Requirements

- Python 3.x
- `requests` library
- `pytest` library

## Installation

1. Clone the repository or download the project files.
2. Install the required libraries using pip:
pip install requests pytest

## Usage

To use the Chuck Norris API module in your Python code, follow these steps:

1. Import the necessary functions from the `chuck_norris_api` module:
```python
from chuck_norris_api import get_random_joke, get_categories, get_random_joke_from_category, get_jokes_count_in_category

Call the desired function to retrieve jokes or categories:

get_random_joke(): Retrieves a random joke.
get_categories(): Retrieves a list of joke categories.
get_random_joke_from_category(category): Retrieves a random joke from a specific category.
get_jokes_count_in_category(category): Retrieves the count of jokes in a specific category.



## Testing

The project includes unit tests to ensure the correctness of the implemented functions. To run the tests, use the
following command:
Copy codepytest test_chuck_norris_api.py
pytest test_chuck_norris_api_with_mocks.py
pytest test_chuck_norris_api_with_parametrize.py
The tests cover various scenarios, including valid and invalid API responses, and use mocking techniques to simulate API
responses without making actual API calls.

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an
issue or submit a pull request on the project's GitHub repository.
License
This project is open-source and available under the MIT License.

## Acknowledgements

This project utilizes the Chuck Norris API (https://api.chucknorris.io/) to retrieve jokes and categories. Special
thanks to the creators and maintainers of the API for providing this entertaining resource.#
