import random
import string


def get_random_password(length=8):
    random_source = string.ascii_letters + string.digits
    password = ''.join(random.sample(random_source,  length))
    return password


print(get_random_password())
