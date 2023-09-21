# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

import os

def split_file_path(file_path):
    # Используем функцию os.path.splitext для разделения имени файла и его расширения
    file_name, file_extension = os.path.splitext(os.path.basename(file_path))
    # Используем функцию os.path.dirname для получения пути к файлу
    file_directory = os.path.dirname(file_path)
    
    return file_directory, file_name, file_extension

# Пример использования функции
file_path = "/путь/к/файлу/имя_файла.txt"
path, name, extension = split_file_path(file_path)
print("Путь:", path)
print("Имя файла:", name)
print("Расширение файла:", extension)
