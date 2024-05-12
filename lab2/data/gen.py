import random


# Генерация массива объектов
def generate_objects_array(size):
    objects = []
    for i in range(size):
        obj = {
            "key": random.choice(["name", "age", "country"]),
            "value": random.randint(1, 100)
        }
        objects.append(obj)
    return objects
