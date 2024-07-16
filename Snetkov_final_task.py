import pandas as pd
filename = 'housing_data.csv'


def read_file(filename: str) -> list[dict]:  # Чтение файла и преобразование его в список словарей
    df = pd.read_csv(filename,
                     dtype={'floor_count': int, 'population': int, 'heating_value': float, 'area_residential': float})
    houses = df.to_dict(orient='records')

    return houses


"""
def read_file(filename: str) -> list[dict]:  # Альтернативный вариант
    with open(filename, 'r', encoding='utf-8') as file:
        import csv
        houses = list(csv.DictReader(file))  # возврат каждой строки в виде словаря
        for row in houses:
            row['floor_count'] = int(row['floor_count'])
            row['population'] = int(row['population'])
            row['heating_value'] = float(row['heating_value'])
            row['area_residential'] = float(row['area_residential'])
    return houses
"""


def classify_house(floor_count: int) -> str:  # Классификация дома на основе количества этажей
    if not floor_count >= 0:
        raise ValueError("Число этажей должно быть положительным!")  # Число проверяется на отрицательность
    if not float(floor_count).is_integer():
        raise TypeError("Количество этажей должно быть целочисленным!")  # Число проверяется на наличие плавающей точки
    if 1 <= floor_count <= 5:
        return "Малоэтажный"
    elif 6 <= floor_count <= 16:
        return "Среднеэтажный"
    elif floor_count > 16:
        return "Многоэтажный"


def get_classify_houses(houses: list[dict]) -> list[str]:  # Классификация домов на основе количества этажей
    categories = []
    for row in houses:
        floor_count = row['floor_count']
        category = classify_house(floor_count)
        categories.append(category)
    return categories


def get_count_house_categories(categories: list[str]) -> dict[str, int]:  # Категорирование домов
    categories_dict = {}
    for house_type in categories:
        if house_type not in categories_dict:
            categories_dict[house_type] = 1
        else:
            categories_dict[house_type] = categories_dict[house_type] + 1
    print(categories_dict)
    return categories_dict


def min_area_residential(houses: list[dict]) -> str:
    area_info = []
    for row in houses:
        area = row["area_residential"] / row["population"]
        area_info.append(area)
    min_area = min(area_info)
    for row in houses:
        check = row["area_residential"] / row["population"]
        if check == min_area:
            address = row["house_address"]
            print('Адрес дома: ', address)
            return address


if __name__ == "__main__":
    houses = read_file(filename)
    classify_houses = get_classify_houses(houses)
    categories = get_count_house_categories(classify_houses)
    address = min_area_residential(houses)
