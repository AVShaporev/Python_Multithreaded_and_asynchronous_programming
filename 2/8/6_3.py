'''
Для иллюстрации работы метода reset (а заодно и пояснения предосторожности при работе с ним) изменим пример так, чтобы нарочно вызывать ошибку при работе 4-го потока - участника:
'''

import threading
from time import sleep


def finalizer():
    print(f"last thread {threading.current_thread().name} stage done")


barrier = threading.Barrier(4, action=finalizer)


def multi_stage_task(i):
    sleep(i)  # эмуляция работы первого этапа
    print(f"{threading.current_thread().name} stage 1")
    try:
        barrier.wait(timeout=2.5)  # ожидаем завершения работы первого этапа всех участников
    except threading.BrokenBarrierError:
        print(f"{threading.current_thread().name} BrokenBarrierError stage 1")
        barrier.reset()

    sleep(i)  # эмуляция работы второго этапа
    print(f"{threading.current_thread().name} stage 2")
    try:
        n = barrier.wait()  # ожидаем завершения работы второго этапа всех участников
        if n == 0:
            print(f"{threading.current_thread().name} multi_stage_task done")
    except threading.BrokenBarrierError:
        print(f"{threading.current_thread().name} BrokenBarrierError stage 2")


thr = [threading.Thread(target=multi_stage_task, args=(i, )) for i in range(4)]
for t in thr:
    t.start()

sleep(10)
print(barrier.n_waiting)

'''
Здесь запускаем 4 потока. Последний поток не успевает за заданный тайм-аут в 2.5 секунды проснутся и вызвать метод wait. Барьер ломается, возбуждается исключение, по которому мы хотим сбросить барьер. Кажется уместным сбросить барьер чтобы продолжить выполнение хотя бы второго этапа. Но, программа не выполняется, а синхронизация работы двух этапов нарушена. Вывод в консоль программы такой:
'''

# Thread-1 (multi_stage_task) stage 1
# Thread-2 (multi_stage_task) stage 1
# Thread-3 (multi_stage_task) stage 1
# Thread-2 (multi_stage_task) BrokenBarrierError stage 1Thread-3 (multi_stage_task) BrokenBarrierError stage 1Thread-1 (multi_stage_task) BrokenBarrierError stage 1


# Thread-1 (multi_stage_task) stage 2
# Thread-4 (multi_stage_task) stage 1
# Thread-2 (multi_stage_task) stage 2
# Thread-3 (multi_stage_task) stage 2
# last thread Thread-3 (multi_stage_task) stage done
# Thread-1 (multi_stage_task) multi_stage_task done
# Thread-4 (multi_stage_task) stage 2
# 1
