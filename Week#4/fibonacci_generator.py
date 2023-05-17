def fibonacci(n):
    a, b = 0, 1
    i = 0
    while i <= n:
        print(f'{i}:', end=' ')
        yield a  # return a, + запам'ятовує місце рестарту для наступного виклику
        a, b = b, a + b
        i += 1


for number in fibonacci(5):  # Використовуємо генератор как ітератор
    print(number)