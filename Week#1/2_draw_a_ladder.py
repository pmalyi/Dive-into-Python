'''
Малюємо драбину.
Це завдання трохи складніше попереднього і вимагатиме від вас роздумів. Необхідно написати скрипт, який "намалює"
(виведе на консоль) сходи. Кількість сходів у сходах передається скрипту як параметр. Гарантується, що на вхід подаються
лише цілі числа > 0. Читання даних потрібно зробити способом, аналогічним тому, що описано у попередньому завданні.
Щаблі повинні відображатися за допомогою символу решітки "#" та пробілів. Приклад роботи скрипта:
11
$ python solution.py 3
  #
 ##
###
$ python solution.py 5
    #
   ##
  ###
 ####
#####

На що звернути увагу? Висновок повинен містити лише пробіли та символ "#". Перший рядок виводу не повинен бути порожнім.
Рядки виведення сходів не повинні містити зайвих прогалин на початку та в кінці рядка. Допускається наявність порожнього
рядка після виведення останнього рядка, що містить щаблі. Наприклад так:
$ python solution.py 5
    #
   ##
  ###
 ####
#####
'''

import sys
n = int(sys.argv[1])
for i in range(1, n + 1):
    print((n - i) * ' ' + i * '#')

'''
solution from coursera: 

import sys
num_steps = int(sys.argv[1])
for i in range(num_steps):
    print(" " * (num_steps - i - 1), "#" * (i + 1), sep="")
'''