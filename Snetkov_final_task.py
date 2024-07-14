import csv

# Чтение файла и преобразование его в список словарей
global param_filename


def read_file():

    with open(
        "housing_data.csv", "r", encoding="utf-8"
    ) as file:  # открытие файла для чтения + замена кодировки
        global param_filename
        param_filename = list(
            csv.DictReader(file)
        )  # возврат каждой строки в виде словаря
        for row in param_filename:
            row["floor_count"] = int(row["floor_count"])
            row["population"] = int(row["population"])
            row["heating_value"] = float(row["heating_value"])
            row["area_residential"] = float(row["area_residential"])

    return param_filename


# Классификация дома на основе количества этажей:


def classify_house():
    param_floor_count = float(
        input("Введите количество этажей: ")
    )  # Ввод количества этажей от пользователя
    if not param_floor_count >= 0:
        raise ValueError(
            "Число этажей должно быть положительным!"
        )  # Введенное число проверяется на отрицательность
    if not param_floor_count.is_integer():
        raise TypeError(
            "Количество этажей должно быть целочисленным!"
        )  # Число проверяется на наличие плавающей точки
    if 1 <= param_floor_count <= 5:
        return "Малоэтажный"
    elif 6 <= param_floor_count <= 16:
        return "Среднеэтажный"
    elif param_floor_count > 16:
        return "Многоэтажный"


# print(classify_house()) # Проверка вывода правильной категории

# Классификация домов на основе количества этажей


global param_houses


def get_classify_houses():
    read_file()
    global param_houses
    param_houses = [{}]
    small = {"house_type": "Малоэтажный"}
    medium = {"house_type": "Среднеэтажный"}
    large = {"house_type": "Многоэтажный"}
    for row in param_filename[1:]:
        row["floor_count"] = int(row["floor_count"])
        row["population"] = int(row["population"])
        row["heating_value"] = float(row["heating_value"])
        row["area_residential"] = float(row["area_residential"])

        if 1 <= row["floor_count"] <= 5:
            row = {**dict(row), **small}
            param_houses.append(row)

        elif 6 <= row["floor_count"] <= 16:
            row = {**dict(row), **medium}
            param_houses.append(row)

        elif row["floor_count"] > 16:
            row = {**dict(row), **large}
            param_houses.append(row)

    return param_houses


# Категорирование домов


count_houses = None


def get_count_house_categories():
    get_classify_houses()
    param_categories = ["Малоэтажный", "Среднеэтажный", "Многоэтажный"]
    global count_houses
    count_houses = []
    sm = 0
    me = 0
    la = 0
    for row in param_houses:
        if row.get("house_type") == "Малоэтажный":
            sm = sm + 1
        elif row.get("house_type") == "Среднеэтажный":
            me = me + 1
        elif row.get("house_type") == "Многоэтажный":
            la = la + 1
    count_houses = [sm, me, la]
    count_houses = dict(zip(param_categories, count_houses))
    return count_houses


get_count_house_categories()


print(count_houses)

houses = None

global area


def min_area_residential():
    get_classify_houses()
    area_info = []
    global houses
    for row in param_houses[1:]:
        global area
        area = row["area_residential"] / row["population"]
        area_info.append(area)
    min_area = min(area_info)
    # print(min_area)

    for row in param_houses[1:]:
        check = row["area_residential"] / row["population"]
        if check == min_area:
            houses = row["house_address"]
            # print(f'Адрес дома: ', row['house_address'])

    return houses


min_area_residential()


print("Адрес дома с наименьшим средним количеством квадратных метров жилой площади на одного жильца: ", houses)
