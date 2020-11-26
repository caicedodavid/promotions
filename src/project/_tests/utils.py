import string
import random
from typing import List, Callable


def random_string(length: int) -> str:
    return ''.join(
        [
            random.choice(string.ascii_letters)
            for _ in range(length)
        ]
    )


def get_data(quantity: int, creator: Callable) -> List:
    return [creator() for _ in range(quantity)]


def generate_ids():
    n = 1
    while True:
        yield n
        n += 1


ids = generate_ids()
