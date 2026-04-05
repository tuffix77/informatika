# TODO импортировать необходимые модули
import json  # Импорт модуля для работы с JSON форматом
import csv  # Импорт модуля для работы с CSV форматом

INPUT_FILENAME = "input.csv"  # Константа с именем исходного CSV файла
OUTPUT_FILENAME = "output.json"  # Константа с именем выходного JSON файла


def task():  # Определение функции task
    # Чтение CSV файла
    with open(INPUT_FILENAME,
              'r') as csv_file:  # Открываем CSV файл в режиме чтения, переменная csv_file ссылается на файл
        csv_reader = csv.DictReader(csv_file,
                                    delimiter=',')  # Создаем DictReader, который преобразует каждую строку в словарь, ключи - заголовки первой строки, разделитель - запятая
        data_list = list(
            csv_reader)  # Преобразуем все строки из csv_reader в список словарей и сохраняем в переменную data_list

    # Запись в JSON файл
    with open(OUTPUT_FILENAME,
              'w') as json_file:  # Открываем JSON файл в режиме записи, переменная json_file ссылается на файл
        json.dump(data_list, json_file,
                  indent=4)  # Сериализуем data_list в JSON формат и записываем в json_file, добавляем отступы в 4 пробела для читаемости


if __name__ == '__main__':  # Проверяем, запущен ли скрипт напрямую (а не импортирован как модуль)
    # Нужно для проверки
    task()  # Вызываем функцию task для выполнения основной работы

    with open(OUTPUT_FILENAME) as output_file:  # Открываем созданный JSON файл для чтения
        for single_line in output_file:  # Перебираем каждую строку в файле
            print(single_line, end="")  # Выводим строку без добавления лишнего перевода строки (end="")