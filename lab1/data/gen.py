import csv
import random


def generate_plants_data(size):
    flowers = ["Роза", "Тюльпан", "Пион", "Лилия", "Орхидея"]
    colors = ["Красный", "Желтый", "Розовый", "Белый", "Фиолетовый"]
    aromas = ["Сильный", "Умеренный", "Слабый"]
    regions = ["Европа", "Азия", "Африка", "Америка", "Австралия"]

    data = []
    for _ in range(size):
        flower = random.choice(flowers)
        color = random.choice(colors)
        aroma = random.choice(aromas)
        region = random.choice(regions)
        data.append([flower, color, aroma, region])

    return data


def write_to_csv(filename, data):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(
            ["Название цветка", "Цвет", "Аромат", "Регионы распространения"]
        )
        writer.writerows(data)


data = generate_plants_data(100000)
write_to_csv("plants.csv", data)
