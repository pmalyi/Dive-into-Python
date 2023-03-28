# Key-value сховище (по зразку з coursera)
'''
Вітаємо з першою повноцінною програмою на Python у рамках нашого курсу! Вона була помітно складніша за попередні і допомогла
вам розібратися відразу з кількома моментами. Хорошим підходом було б розбити свою програму на функції, зверніть увагу,
всі команди винесені в окремі функції, а read_data ми використовуємо в кількох місцях. Ключовим моментом у розробці будь-якої
програми є вибір відповідної структури даних. У цьому прикладі логічним варіантом було використовувати словник, тому що він
по суті є key-value сховищем, а значення просто зберігати в списку.

Також у цьому завданні ми використовували модуль argparse для зчитування аргументів командного рядка та json для зберігання даних
у файлі. Найпростішим підходом було просто перечитувати при кожному зверненні файл, перетворюючи його на словник, додаючи значення
за необхідності. Модуль os допомагає нам у перевірці існування файлу сховища під час першого запуску програми. У Python багата
стандартна бібліотека, дуже важливо уявляти собі, які модулі допоможуть нам у вирішенні наших завдань, і вміти швидко розбиратися
в документації до нових функцій.
'''


import json
import os
import tempfile
import argparse


def read_data(storage_path):
    if not os.path.exists(storage_path):
        return {}
    with open(storage_path, 'r') as inF:
        raw_data = inF.read()
        if raw_data:
            return json.loads(raw_data)
        return {}


def write_data(storage_path, data):
    with open(storage_path, 'w') as outF:
        outF.write(json.dumps(data))


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', help='Key')
    parser.add_argument('--val', help='Value')
    return parser.parse_args()


def put(storage_path, key, value):
    data = read_data(storage_path)
    data[key] = data.get(key, list())
    data[key].append(value)
    write_data(storage_path, data)


def get(storage_path, key):
    data = read_data(storage_path)
    return data.get(key, [])


def main(storage_path):
    arg = parse()
    if arg.key and arg.val:
        put(storage_path, arg.key, arg.val)
    elif arg.key:
        print(*get(storage_path, arg.key), sep=', ')
    else:
        print('The program is called with invalid parameters.')


if __name__ == '__main__':
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    main(storage_path)
