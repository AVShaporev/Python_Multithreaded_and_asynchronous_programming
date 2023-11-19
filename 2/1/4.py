import threading
from time import sleep, perf_counter


# def task():
#     print(f"-strating task with {threading.current_thread().name}, {threading.active_count()=}")
#     sleep(1)
#     print(f"-----end task with {threading.current_thread().name}")


# task()
# thr_1 = threading.Thread(target=task)
# thr_1.start()
# thr_1.join()

# print(f"{threading.active_count()=}")
# print("END MAIN")


import threading
from time import sleep

result = "*"


def test(time_sleep: float | int = 0, s: str = "*"):
    global result
    sleep(time_sleep)
    result += f"--{s}"


test()
thr_1 = threading.Thread(target=test, args=(1, "1"))
thr_1.start()
thr_2 = threading.Thread(target=test, args=(2, "2"))
thr_2.start()
# thr_2.join()    #!!!

# print(result)

start_t = perf_counter()
thr_1.join(1.5)
print(f"1 - {perf_counter() - start_t}")

start_t = perf_counter()
thr_2.join(2.2)
print(f"2 - {perf_counter() - start_t}")


print(result)

# *--*!