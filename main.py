import time
import json
from pick import pick
from random import randint


SelectSortBigO = "n^2"
def selection_sort(x_list: list, r:int):
    for i in range(0, r - 1):
        smallest = i
        for j in range(i + 1, r):
            if x_list[j] < x_list[smallest]:
                smallest = j
        x_list[i], x_list[smallest] = x_list[smallest], x_list[i]
    return x_list

def inter_sort():
    title = "Выберите сортировку:"

    options = {
        f"Ввести свои данные": create_mas,
        f"сортировка с рандомными данными":create_random_data,
    }

    option, index = pick([key for key, value in options.items()], title)
    options[option]()


def read_data(file_name: str = "data.json"):
    with open(file_name, "r") as file:
        data = json.load(file)        
    return data

def write_data(data: list, file_name: str = "data.json"):
    with open(file_name, "w") as f:
        json.dump(data, f)


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
    write_data(int_lst)
    do_sort()

    


def sort_time(data: list):
    start_time = time.time()
    selection_sort(data, len(data))
    end_time = time.time()
    
    return end_time-start_time

def print_info(time_to_sort, file_name, data):
    print(f"Затраченое время: {time_to_sort} сек.")
    print(f"Количество элементов в масиве: {len(data)}")
    print(f"Файл с массивом: {file_name}")


    enter_data = read_data(file_name)
    enter_data.sort()
    print(f"\nПроверка правильности сортировки: {enter_data == data}")
    
    print(f"Сложность алгоритма по нотации Big O: {SelectSortBigO}")
    input("Для выхода в меню нажмите Enter")
    print("-"*32)
    print("")
    menu_main()

def do_sort(amount_items: int = 10_000, file_name: str = "data.json"):
    data = read_data(file_name)
    time_to_sort = sort_time(data)
    print_info(time_to_sort, file_name, data)

def create_random_data(amount_items: int = 10_000, file_name: str = "data.json"):
    data_list = []
    for i in range(amount_items):
        data_list.append(randint(-10_000, 10_000))

    write_data(data_list, file_name)
    do_sort()


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
        f"Выполнить сортировку": inter_sort,
        f"Изменить количество объектов: {settings[0]} (Текущее значение)": amount_change,
        f"Изменить файл: {settings[1]} (Текущий файл)": file_change,
        f"Главное меню": menu_main,
    }

    option, index = pick([key for key, value in options.items()], title)
    if index in [1, 2]:
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
