"""
У нас есть класс FileHandler, который может считывать файлы, но не всегда в удобном для нас виде.
Поэтому мы создали два его наследника: CSVHandler и JSONHandler

Задания:
    1. Переопределите метод read у CSVHandler и JSONHandler
    2. Метод read у JSONHandler должен возвращать словарь. Для этого используйте модуль встроенный модуль json
    3. Метод read у CSVHandler должен возвращать список словарей. Для этого используйте модуль встроенный модуль csv
    4. Создайте экземпляры каждого из трех классов.
       С помощью экземпляра FileHandler прочитайте и распечатайте содержимое файла text.txt
       С помощью экземпляра JSONHandler прочитайте и распечатайте содержимое файла recipes.json
       С помощью экземпляра CSVHandler прочитайте и распечатайте содержимое файла user_info.csv

"""
import csv
import json


class FileHandler:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, 'r') as file:
            return file.read()


class JSONHandler(FileHandler):
    def read(self):
        with open(self.filename, 'r') as file:
            return json.load(file)


class CSVHandler(FileHandler):
    def read(self):
        with open(self.filename, 'r') as file:
            return csv.load(file)


if __name__ == '__main__':
   # Создаем экземпляры каждого из трех классов
    file_handler = FileHandler("data/text.txt")
    json_handler = JSONHandler("data/recipes.json")
    csv_handler = CSVHandler("data/user_info.csv")

    # С помощью экземпляра FileHandler прочитайте и распечатайте содержимое файла text.txt
    print("FileHandler:")
    print(file_handler.read())

    # С помощью экземпляра JSONHandler прочитайте и распечатайте содержимое файла recipes.json
    print("\nJSONHandler:")
    print(json_handler.read())

    # С помощью экземпляра CSVHandler прочитайте и распечатайте содержимое файла user_info.csv
    print("\nCSVHandler:")
    print(csv_handler.read())
