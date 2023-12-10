'''
Для того, чтобы выполнить завершающее действие в каждом этапе последним потоком - участником вызвавшем метод wait, укажем в аргументе объекта барьера action функцию финализатора. А для того, чтобы выполнить завершающее действие после всех этапов, в целевой задаче используем условие равенства результата вызова метода wait нулю:
'''

import threading
from time import sleep
from random import randint


def finalizer():
    print(f"last thread {threading.current_thread().name} stage done")


barrier = threading.Barrier(4)    # , action=finalizer


def multi_stage_task():
    sleep(randint(0, 4))  # эмуляция работы первого этапа
    print(f"{threading.current_thread().name} stage 1")
    barrier.wait()  # ожидаем завершения работы первого этапа всех участников

    sleep(randint(0, 4))  # эмуляция работы второго этапа
    print(f"{threading.current_thread().name} stage 2")
    n = barrier.wait()  # ожидаем завершения работы второго этапа всех участников
    if n == 0:
        finalizer()                         #print(f"{threading.current_thread().name} multi_stage_task done")



thr = [threading.Thread(target=multi_stage_task) for _ in range(4)]
for t in thr:
    t.start()


'''
Thread-4 (multi_stage_task) stage 1
Thread-2 (multi_stage_task) stage 1
Thread-3 (multi_stage_task) stage 1
Thread-1 (multi_stage_task) stage 1
last thread Thread-1 (multi_stage_task) stage done
Thread-3 (multi_stage_task) stage 2
Thread-4 (multi_stage_task) stage 2Thread-1 (multi_stage_task) stage 2

Thread-2 (multi_stage_task) stage 2
last thread Thread-2 (multi_stage_task) stage done
Thread-3 (multi_stage_task) multi_stage_task done
'''