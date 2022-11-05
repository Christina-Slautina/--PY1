import pprint


def new_dict(num):
    this_dict = {'bin': bin(num), 'dec': num, 'hex': hex(num), 'oct': oct(num)}
    return this_dict


my_dict = [new_dict(x) for x in range(16)]
pprint.pprint(my_dict)
