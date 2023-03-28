'''
Сума цифр у рядку
Давайте почнемо з нескладного завдання. Ваша мета написати програму (скрипт), яка запускатиметься з командного рядка.
Програма приймає як аргумент рядок, що складається з цифр. Гарантується, що інших символів у переданому параметрі немає
і на вхід завжди подається рядок. Програма повинна обчислити суму цифр, з яких складається рядок і вивести отриманий
результат на друк у стандартний вивід.

Приклади роботи програми:
$ python solution.py 12345
15
$ python solution.py 160438521039
42

Зчитувати переданий параметр можна за допомогою модуля стандартної бібліотеки sys:
import sys

digit_string = sys.argv[1]

Виконання цього коду створить змінну digit_string, значенням якої буде рядок, переданий у параметрі під час запуску
вашої програми. Докладніше про модуль sys та передачу параметрів у скрипт ви можете прочитати в документації до модуля sys.

Файл із програмою має називатися solution.py. Після написання та налагодження вашого рішення вам необхідно завантажити
файл solution.py на платформу для перевірки.
'''

import sys
digit_string = sys.argv[1]
sum = 0
for digit in digit_string:
    sum = sum + int(digit)
print(sum)

'''
solution from coursera:

import sys
print(sum([int(x) for x in sys.argv[1]]))
'''