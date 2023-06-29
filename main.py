import time
import json
from pick import pick
from random import randint

SelectSortBigO = "n^2"

def create_mas():
    print("Введите последовательность чисел:")
    list_data = input().split()
    int_lst = []
    for element in list_data:
        if element.isdigit():
            int_lst.append(int(element))
        else:
            print(f'{element} - не является числом ')
            print('Ошибка формирования списка чисел')
            menu_main()
    with open("data.json", "w") as f:
        json.dump(int_lst, f)
    menu_main()

def selection_sort(x_list: list):
    for i in range(0, len(x_list) - 1):
        smallest = i
        for j in range(i + 1, len(x_list)):
            if x_list[j] < x_list[smallest]:
                smallest = j
        x_list[i], x_list[smallest] = x_list[smallest], x_list[i]
    return x_list


def do_sort(amount_items: int = 10_000, file_name: str = "data.json"):
    create_random_data(amount_items, file_name)

    with open(file_name, "r") as file:
        data = json.load(file)

    start_time = time.time()
    selection_sort(data)
    end_time = time.time()

    print(f"Затраченое время: {end_time-start_time} сек.")
    print(f"Количество элементов в масиве: {len(data)}")
    print(f"Файл с массивом: {file_name}")

    with open(file_name, "r") as file:
        enter_data = json.load(file)
        enter_data.sort()
        print(f"\nПроверка правильности сортировки: {enter_data == data}")
    print(f"Сложность алгоритма по нотации Big O: {SelectSortBigO}")
    input("Для выхода в меню нажмите Enter")
    print("-"*32)
    print("")
    menu_main()


def create_random_data(amount_items: int = 10_000, file_name: str = "data.json"):
    data_list = []
    for i in range(amount_items):
        data_list.append(randint(-10_000, 10_000))

    with open(file_name, "w") as write_file:
        json.dump(data_list, write_file)


def amount_change(settings: list):
    try:
        inp = int(input("Новое количество элементов в массиве: "))
        settings[0] = inp
    except ValueError:
        print("Ошибка ввода! Введите число")
        amount_change(settings)
    menu_sort_with_settings(settings)


def file_change(settings: list):
    inp = input("Имя файла: ")
    settings[1] = inp
    menu_sort_with_settings(settings)


def menu_sort_with_settings(settings: list = [10_000, "data.json"]):
    title = "Меню редактирования настроек"

    options = {
        f"Выполнить сортировку": do_sort,
        f"Изменить количество объектов: {settings[0]} (Текущее значение)": amount_change,
        f"Изменить файл: {settings[1]} (Текущий файл)": file_change,
        f"Главное меню": menu_main,
        f"Задать свой массив": create_mas,
    }

    option, index = pick([key for key, value in options.items()], title)
    if index == 0:
        do_sort(settings[0], settings[1])
    elif index in [1, 2]:
        options[option](settings)
    else:
        options[option]()


def menu_main():
    title = "При выполнении сортировки создается массив чисел (от -10 000 до 10 000) в файле 'data.json'\n" \
            "Задать количество объектов в массиве и выбрать другой файл можно с помощью Сортировки с настройками\n"

    options = {
        "Выполнить сортировку": do_sort,
        "Сортировка с настройками": menu_sort_with_settings
    }
    option, index = pick([key for key, value in options.items()], title)
    options[option]()


if __name__ == '__main__':
    menu_main()
