import threading
import time


def task(function, *args, **kwargs):
    print(f"{'started_task':-^70}")
    print(f"{threading.current_thread().name=}, {threading.active_count()=}")
    function(*args, **kwargs)
    print(f"{'end_task':-^70}")




tasks =[]

for i in range(20):
    tasks.append(threading.Thread(target=task, args=(time.sleep, 0.1)))

for task in tasks:
    task.start()

# thr_1 = threading.Thread(target=task, args=(print, "Здесь тоже могла быть Ваша реклама!!!"))
# thr_1.name = "Thread_1!!!"
# thr_1.start()
