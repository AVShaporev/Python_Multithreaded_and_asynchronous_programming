import threading

# Создайте объект барьера
barrier = threading.Barrier(4)

# Создайте целевую функцию, выполняющую задачи в два этапа
def task(barrier, task_st_1, task_st_2):
    task_st_1()
    barrier.wait()

    task_st_2()
    n = barrier.wait()

    if n == 0:
        finalizer()

# Создайте и запустите 4 потока
thr = [threading.Thread(target=task) for _ in range(4)]
for t in thr:
    t.start()