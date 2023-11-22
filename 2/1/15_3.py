# import threading
# from time import sleep


# def task():
#     sleep(0.5)
#     raise Exception("!!! exception in task !!!")


# thread_1 = threading.Thread(target=task)
# thread_1.start()


import threading
from time import sleep


def custom_hook(arg):
    print(arg)
    print(f"{threading.current_thread().name=} failed")


def task():
    sleep(0.5)
    raise Exception("!!! exception in task !!!")


threading.excepthook = custom_hook

thread_1 = threading.Thread(target=task)
thread_1.start()