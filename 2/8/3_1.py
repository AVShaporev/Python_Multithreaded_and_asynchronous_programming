'''
Если запустить такой код, то мы ожидаемо увидим последовательную распечатку строки каждым потоком из десяти по очереди. Каждый поток будет поднимать семафор, а следующие будут вынуждены ждать, т.к. у нас стоит ограничение внутреннего счетчика в единицу
'''

import threading
import time


def task(sema: threading.Semaphore, text):
    with sema:
        print(f"thread id = {threading.current_thread().ident} print {text}")
        time.sleep(1)


# semaphore = threading.Semaphore()
semaphore = threading.Semaphore(5) # Если указать значение 5, то: во-первых, наш код выполнится быстрее (ведь одновременно за раз будут выполняться сразу 5 потоков), во-вторых, мы можем наблюдать эффект состояния гонки, т.к. печать могут выполнять уже несколько потоков одновременно.

thr = []
for i in range(10):
    thr.append(threading.Thread(target=task, args=(semaphore, i)))
for t in thr:
    t.start()