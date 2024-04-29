from chuck_norris_api import *
import random

def main():
    print(get_random_joke())
    print(get_categories())
    print(get_random_joke_from_category(random.choice(get_categories())))
    print(get_jokes_count_in_category(random.choice(get_categories())))

if __name__ == "__main__":
    main()