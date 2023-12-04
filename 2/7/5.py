import threading
import time
from random import uniform

lock = threading.Lock()


def test():
    lock.acquire(blocking=True, timeout=5)
    time.sleep(uniform(0, 1))
    print(f"{threading.current_thread().name=}, {lock.locked()=}")


thr = [threading.Thread(target=test) for _ in range(5)]
for t in thr:
    t.start()
for t in thr:
    t.join()

print(lock.locked())
print("END")