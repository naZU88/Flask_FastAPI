'''Синхронный подход'''
import time

# Эта программа вызывает функцию slow_function(), которая занимает 5 секунд на
# выполнение. Весь код работает синхронно, то есть выполнение программы
# блокируется на время выполнения функции.

def slow_function():
    print("Начало функции")
    time.sleep(5)
    print("Конец функции")

print("Начало программы")
slow_function()
print("Конец программы")