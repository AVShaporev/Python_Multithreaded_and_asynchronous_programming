import threading
import time
from random import uniform

lock = threading.Lock()


def test():
    # print(lock.locked())
    time.sleep(uniform(0, 1))
    lock.acquire(blocking=False)
    print(f"{threading.current_thread().name=}, {lock.locked()=}")
    # lock.release()



thr = [threading.Thread(target=test) for _ in range(5)]
for t in thr:
    print(f"{threading.current_thread().name=}, {lock.locked()=}")
    t.start()
for t in thr:
    print(f"{threading.current_thread().name=}, {lock.locked()=}")
    t.join()

print(f"{threading.current_thread().name=}, {lock.locked()=}")
print(lock.locked())
print("END")