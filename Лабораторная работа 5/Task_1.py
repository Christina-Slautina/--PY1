import pprint


def get_dictionary(num):
    dictionary = {'bin': bin(num), 'dec': num, 'hex': hex(num), 'oct': oct(num)}
    return dictionary


my_dictionary = [get_dictionary(num) for num in range(16)]
pprint.pprint(my_dictionary)
