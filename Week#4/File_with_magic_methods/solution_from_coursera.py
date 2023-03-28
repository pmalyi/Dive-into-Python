# Файли з магічними методами від Coursera
'''
Рішення

У цьому завданні потрібно було акуратно реалізувати кілька класичних магічних методів та кілька звичайних. При ініціалізації
ми зберігаємо шлях, а також можемо перевірити існування файлу, хоча це не потрібно під час тестування. Методи write і read просто
працюють із файлом у системі. Хоча наявності методу для читання не вимагалося, його реалізація допомагає нам у роботі інших функцій,
та й взагалі - який write без read.

Метод __str__ навряд чи викликав у вас проблеми, інші методи цікавіші. При додаванні файлів на нас лягає завдання вибору імені нового файлу.
В умові про назву нічого не сказано, і в реальних завданнях майже завжди над такими деталями доводиться думати самостійно. У прикладі ми
генеруємо ім'я за допомогою модуля uuid (href='https://docs.python.org/3/library/uuid.html'), який дозволяє створювати ідентифікатори UUID (href='https://en.wikipedia.org/wiki/Universally_unique_identifier').
Файл ми зберігаємо в тій же директорії, що й існуючий, що допомагає уникнути проблем із правами (можна використовувати gettempdir як в умові).

Під час ітерації головним питанням є збереження номера прочитаного рядка. Найпростішим варіантом було б просто повернути ітератор рядків,
наприклад, за допомогою методу readlines. Однак, у такому випадку ми читаємо відразу весь файл, який може бути дуже великим і який нам
може бути і не потрібен. У нашому рішенні ми зберігаємо поточну позицію у файлі за допомогою методу tell та використовуємо readline
для отримання єдиного наступного рядка. Після закінчення читання файлу метод викидає StopIteration, як кожний поважаючий себе ітератор.
Можна також використовувати те, що файловий об'єкт в Python сам по собі є ітератором.
'''

import os
import uuid


class File:
    def __init__(self, path):
        self.path = path
        self.current_position = 0

        if not os.path.exists(self.path):
            open(self.path, 'w').close()

    def write(self, content):
        with open(self.path, 'w') as f:
            return f.write(content)

    def read(self):
        with open(self.path, 'r') as f:
            return f.read()

    def __add__(self, obj):
        new_path = os.path.join(
            os.path.dirname(self.path),
            str(uuid.uuid4().hex)
        )
        new_file = type(self)(new_path)
        new_file.write(self.read() + obj.read())

        return new_file

    def __str__(self):
        return self.path

    def __iter__(self):
        return self

    def __next__(self):
        with open(self.path, 'r') as f:
            f.seek(self.current_position)

            line = f.readline()
            if not line:
                self.current_position = 0
                raise StopIteration('EOF')

            self.current_position = f.tell()
            return line
