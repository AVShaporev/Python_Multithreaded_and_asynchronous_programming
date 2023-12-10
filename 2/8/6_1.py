'''
Рассмотрим пример целевой задачи, которая включает в себя два этапа, причем последующий этап должен дождаться завершения выполнения предыдущего этапа всеми потоками - участниками.
'''


import threading
from time import sleep
from random import randint


barrier = threading.Barrier(4)  # объект барьера для 4 участников


def multi_stage_task():
    sleep(randint(0, 4))  # эмуляция работы первого этапа
    print(f"{threading.current_thread().name} stage 1")
    barrier.wait()  # ожидаем завершения работы первого этапа всех участников

    sleep(randint(0, 4))  # эмуляция работы второго этапа
    print(f"{threading.current_thread().name} stage 2")
    barrier.wait()  # ожидаем завершения работы второго этапа всех участников

    print("all threads finished stages")  # выводим на печать после того, как все участники прошли барьер 2-го этапа


thr = [threading.Thread(target=multi_stage_task) for _ in range(4)]
for t in thr:
    t.start()

'''
Thread-2 (multi_stage_task) stage 1
Thread-1 (multi_stage_task) stage 1
Thread-3 (multi_stage_task) stage 1
Thread-4 (multi_stage_task) stage 1
Thread-2 (multi_stage_task) stage 2
Thread-3 (multi_stage_task) stage 2
Thread-4 (multi_stage_task) stage 2
Thread-1 (multi_stage_task) stage 2
all threads finished stages
all threads finished stagesall threads finished stagesall threads finished stages
'''