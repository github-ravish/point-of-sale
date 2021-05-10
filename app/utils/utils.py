import random
import string


ALPHANUMERIC_CHARS = string.digits + \
    string.ascii_uppercase + string.ascii_lowercase
CAPS_NUMERIC = string.digits + string.ascii_uppercase
SLUG_LENGTH = 6
PAYMENT_SLUG_LENGTH = 16


def generate_slug(name, chars=CAPS_NUMERIC, length=SLUG_LENGTH):
    name = name.lower().split()
    name = "-".join(name)
    random_str = "".join(random.choice(chars) for _ in range(length))
    return name + "-" + random_str


def generate_payment_slug(chars=ALPHANUMERIC_CHARS, length=PAYMENT_SLUG_LENGTH):
    return "".join(random.choice(chars) for _ in range(length))
