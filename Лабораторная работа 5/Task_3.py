import random


def get_unique_list_numbers() -> list[int]:
    numbers = random.sample(range(-10, 11), 15)
    unique_list_numbers = list(numbers)
    return unique_list_numbers


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
