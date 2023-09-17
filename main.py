import random
import threading
import time

def pi_op(size):
    inside_circle = 0

    for _ in range(size):
        x, y = random.random(), random.random()
        if x**2 + y**2 <= 1:
            inside_circle += 1

    return (inside_circle / size) * 4

def pi_bp(size, tsize):
    points_per_thread = size // tsize
    threads = []

    inside_circle = 0

    def handler():
        nonlocal inside_circle
        for _ in range(points_per_thread):
            x, y = random.random(), random.random()
            if x**2 + y**2 <= 1:
                inside_circle += 1

    for _ in range(tsize):
        thread = threading.Thread(target=handler)
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    return (inside_circle / size) * 4

size = int(input("Введіть кількість точок для обчислення: "))
tsize = int(input("Введіть кількість потоків: "))

start_time = time.time()
pi_opr = pi_op(size)
end_time = time.time()
print(f"Число Пі (один потік): {pi_opr}")
print(f"Час виконання (один потік): {end_time - start_time} секунд")

start_time = time.time()
pi_bpr = pi_bp(size, tsize)
end_time = time.time()
print(f"Число Пі (багатопотоковість, {tsize} потоки): {pi_bpr}")
print(f"Час виконання (багатопотоковість, {tsize} потоки): {end_time - start_time} секунд")