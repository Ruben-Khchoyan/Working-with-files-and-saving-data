
from Этап_4_Обработка_ошибок import errors


# Импорт модуля yaml
import yaml


# Начало функции чтения файла с заметками
def load_notes_from_file(filename):
    # Кортеж с ключами отображающими смысл данных в нужном формате,
    # для дальнейшей работу других функций
    keys = ('username', 'title', 'content', 'status', 'created_date', 'issue_date')

    # Начало блока try для обработки ошибок
    try:
        # Открытие файла через оператор with, чтобы исключить строку с закрытием файла.
        # encoding='UTF-8', кодировка для работы с русским языком.
        # 'r' - чтение файла с заметками
        # Функция yaml.safe_load для чтения файла и возврата списка заметок(словарей)
        with open(filename + '.yaml', 'r', encoding='UTF-8') as file:
            load_data = yaml.safe_load(file)

        if not load_data: # Если файл пустой, то выводится соответствующая надпись
            print("Файл пустой!")
            return []
        else:
            # Создание нового списка заметок с ключами из keys.
            # Для создания словаря с нужными ключами используется функция zip,
            # которой передается ключи и список значений заметки из словаря.
            # И так для каждой заметки через цикл for
            return list(dict(zip(keys, note.values())) for note in load_data)
    except FileNotFoundError: # Обработка ошибки отсутствия файла
        with open(filename + '.yaml', 'x', encoding='UTF-8'):
            print('Файл filename не найден. Создан новый файл.')
            return []
    except UnicodeDecodeError: # Обработка ошибки чтения файла
        print('Ошибка при чтении файла filename. Проверьте его содержимое.')
    except PermissionError: # Обработка ошибки доступа к файлу
        print('Ошибка доступа! Отсутствие прав доступа!')
# Конец функции


if __name__ == '__main__':
    notes = load_notes_from_file("notes")

    print(notes)