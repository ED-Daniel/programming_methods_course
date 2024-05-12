import csv
import random
from .flower import Flower


def read_plants_data(file_path):
    output = []
    with open(file_path, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            output.append(
                Flower(
                    row["Название цветка"],
                    row["Цвет"],
                    row["Аромат"],
                    row["Регионы распространения"],
                )
            )
    return output


def select_random_subset(arr, length):
    if length > len(arr):
        raise ValueError(
            "Length cannot be greater than the size of the input array"
        )

    random.shuffle(arr)  # перемешиваем массив в случайном порядке
    return arr[:length]  # выбираем первые length элементов
