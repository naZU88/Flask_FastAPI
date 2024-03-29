'''Синхронный подход'''
import random
import time

# Эта программа запускает длительную задачу long_running_task(), которая
# выполняется в течение случайного времени от 1 до 3 секунд. Весь код работает
# синхронно, поэтому выполнение программы блокируется на время выполнения
# задачи.

def long_running_task():
    for i in range(5):
        print(f"Выполнение задачи {i}")
        time.sleep(random.randint(1, 3))

def main():
    print("Начало программы")
    long_running_task()
    print("Конец программы")

main()
