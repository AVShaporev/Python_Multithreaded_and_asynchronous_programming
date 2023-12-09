import threading
from typing import Callable


class HubHendler:
    def __init__(self, n: int, task: Callable, n_threads: int):
        self._task = task
        self._n_threads = n_threads
        self._sema = threading.Semaphore(value=n)

    def start_hub(self):
        
        thr = []
        for i in range(self._n_threads):
            thr.append(threading.Thread(target=self.my_task))
        for t in thr:
            t.start()

        for t in thr:
            t.join()

    def my_task(self):
        self._sema.acquire(blocking=True)
        self._task()
        self._sema.release()
            


def my_print():
    print(f"thread id = {threading.current_thread().ident} {threading.Semaphore.__str__}")

my_semaphore = HubHendler(10, my_print, 20)

my_semaphore.start_hub()