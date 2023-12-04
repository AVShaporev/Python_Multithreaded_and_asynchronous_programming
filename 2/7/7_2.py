import threading
import threading

event_increment = threading.Event()
event_write = threading.Event()

n = 0
lock = threading.Lock()

def task_increment():
    global n
    while n <= 1000:
        with lock:
            with open("f_in.txt", "a") as file:
                n += 1
                tmp = str(n) + "\n"
                file.write(tmp)


def task_write():
    while n <= 1000:
        with lock:
            with open("f_in.txt", "r") as f_read:
                try:
                    x = f_read.read().split()[-1]
                    if x:
                        x = int(x)
                except IndexError as err:
                    print(err)
            if x % 2 == 0:
                with open("f_in.txt", "r") as f_read, open("f_out.txt", "a") as f_out:
                    f_out.write(f"{f_read.read().split()[-1]}\n")