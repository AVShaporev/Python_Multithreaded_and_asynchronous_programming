import queue

my_queue = queue.Queue(maxsize=5)

for elem in range(10):
    print(elem)
    try:
        my_queue.put(elem)
    except queue.Full:
        break

print(my_queue.qsize())