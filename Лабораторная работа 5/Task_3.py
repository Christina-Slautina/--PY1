import random


def get_unique_list_numbers(start=-10, stop=11, size=15):
    random_number_list = []
    while len(random_number_list) < size:
        random_number_list.append(random.randint(start, stop - 1))
        random_number_list = list(set(random_number_list))
    return random_number_list


my_random_number_list = get_unique_list_numbers()
print(my_random_number_list)
print(len(my_random_number_list) == len(set(my_random_number_list)))
