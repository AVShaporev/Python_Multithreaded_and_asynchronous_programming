# Перепишем пример без менеджера контекста:


import threading
import time


def task(sema: threading.Semaphore, text):
    sema.acquire()
    print(f"thread id = {threading.current_thread().ident} print {text}")
    time.sleep(1)
    sema.release(2)  # освобождает сразу два потока


semaphore = threading.Semaphore(2)

thr = []
for i in range(20):
    thr.append(threading.Thread(target=task, args=(semaphore, i)))
for t in thr:
    t.start()

'''
Здесь мы в каждой целевой задаче освобождаем сразу два потока вместо одного, таким образом при выполнении программы наблюдается эффект каскада. Сначала семафор могут поднять только два потока (согласно нашему ограничению value=2). Два потока поднимают семафор, выполняют целевую задачу и в конце каждый из них методом release добавляет двойку к внутреннему счетчику. В следующий момент времени уже 4 потока могут одновременно выполняться. И так по нарастающей. Если в конце выполнения программы вывести состояние внутреннего счетчика семафора, то оно буде равно 22.

Если запустить этот же код, но применить объект ограниченного семафора, в процессе выполнения будут формироваться ошибки вида ValueError: Semaphore released too many times для потоков, выполняющие метод release, в результате которого будет попытка отпустить семафор больше раз чем задано ограничение value.
'''