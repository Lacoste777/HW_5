# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

text = r'C:\Users\Lacoste\Desktop\HW_5\HW_5\Task_1.py'


def file_path(text):
    *path, name = text.split('\\')
    name = list(name.split('.'))
    path = '\\'.join(path)
    expansion = name[1]
    return f'ПУТЬ: {path}, ИМЯ ФАЙЛА: {name[0]}, РАСШИРЕНИЕ: {expansion}'


print(file_path(text))
