import random
import string


def generate_combinations():
    letters = string.ascii_lowercase
    combinations = []

    for letter1 in letters:
        for letter2 in letters:
            combination = letter1 + letter2
            combinations.append(combination)

    return combinations


# Генерация массива объектов
def generate_objects_array(size):
    objects = []
    keys = generate_combinations()
    for i in range(size):
        obj = {
            "key": random.choice(keys),
            "value": random.randint(1, 100)
        }
        objects.append(obj)
    return objects
