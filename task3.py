# Создайте функцию генератор чисел Фибоначчи 
# https://ru.wikipedia.org/wiki/%D0%A7%D0%B8%D1%81%D0%BB%D0%B0_%D0%A4%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Пример использования генератора
fibonacci = fibonacci_generator()
for _ in range(10):  # Генерировать первые 10 чисел Фибоначчи
    print(next(fibonacci))
