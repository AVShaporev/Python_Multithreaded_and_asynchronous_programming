from queue import Queue
from threading import Thread

my_queue = Queue(maxsize=5)
my_queue2 = Queue()


def my_main():
    i = 1
    while True:
        print(i)
        if not my_queue.full():
            my_queue.put(i)
        else:
            my_queue2.put(i)
        i += 1
        if i > 10:
            break


my_thread = Thread(target=my_main, daemon=True)

my_thread.start()
my_thread.join()

while not my_queue.empty():
    print(my_queue.get(), end=' ')

print()

while not my_queue2.empty():
    print(my_queue2.get(), end=' ')