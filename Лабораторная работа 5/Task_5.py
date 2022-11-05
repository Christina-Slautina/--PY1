import random
import string


def get_random_password(n=8):
    random_source = string.ascii_letters + string.digits  # The concatenation of the ascii_lowercase and ascii_uppercase
    password = ''.join(random.sample(random_source, n))
    return password


print(get_random_password())
