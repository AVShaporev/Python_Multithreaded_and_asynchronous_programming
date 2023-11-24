import threading
import queue
# from itertools import count  # для генерации целых чисел
from random import randint
from time import sleep

# queue = queue.Queue(maxsize=10)
# queue = queue.LifoQueue(10)
queue = queue.PriorityQueue(10)
# count = count()

def producer(t: int | float):
    while True:
        # i = next(count)
        i = randint(0, 100)
        queue.put(i)
        print(f"{threading.current_thread().name}\tput\t->\t{i}\tQueue size = {queue.qsize()}")
        sleep(t)

def consumer(t: int | float):
    while True:
        n = queue.get()
        print(f"{threading.current_thread().name}\t<-\tget\t{n}")
        sleep(t)

thread_0 = threading.Thread(target=producer, args=(0.5,), name="producer_0")
thread_1 = threading.Thread(target=producer, args=(0.6,), name="producer_1")
# thread_5 = threading.Thread(target=producer, args=(0.3,), name="producer_1")
# thread_6 = threading.Thread(target=producer, args=(0.3,), name="producer_1")
thread_2 = threading.Thread(target=consumer, args=(1, ), name="consumer_1")
thread_3 = threading.Thread(target=consumer, args=(2, ), name="consumer_2")
thread_4 = threading.Thread(target=consumer, args=(3, ), name="consumer_3")
thread_0.start()
thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()
# thread_5.start()
# thread_6.start()