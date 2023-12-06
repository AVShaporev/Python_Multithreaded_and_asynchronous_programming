import threading
from time import sleep

condition = threading.Condition()


def task(condition: threading.Condition):
    with condition:
        condition.wait()
        print(f"test work done with thread id = {threading.current_thread().ident}")


def producer(condition: threading.Condition, time: int | float = 0):
    with condition:
        sleep(time)
        condition.notify()


thr_1 = threading.Thread(target=task, args=(condition, ), daemon=True)
thr_2 = threading.Thread(target=task, args=(condition, ), daemon=True)
thr_1.start()
thr_2.start()

time_for_producer = 0.5
thr_0 = threading.Thread(target=producer, args=(condition, time_for_producer))
thr_0.start()
thr_1.join(1)
thr_2.join(1)
print("END")