import string
import random


def passwordGenerator(preferredLength):
    password_characters = string.ascii_lowercase + \
        string.ascii_uppercase + string.digits + string.punctuation
    password = list(random.choice(password_characters)
                    for value in range(preferredLength))

    random.shuffle(password)
    return "".join(password)


print(passwordGenerator(10))
