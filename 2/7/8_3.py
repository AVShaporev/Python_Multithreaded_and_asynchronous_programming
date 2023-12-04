import threading
from typing import Callable
from time import perf_counter
from itertools import count


class TestWorker(threading.Thread):
    def __init__(self, task: Callable, permission: Callable, condition: threading.Condition):
        super().__init__()
        self.permission = permission
        self.task = task
        self.condition = condition

    def make_work(self):  # основной метод выполняет задачу если получено условие
        with self.condition:
            start = perf_counter()
            tmp = self.condition.wait_for(predicate=self.permission, timeout=5)
            if tmp:
                self.task()  # выполняем задачу если разрешено
            else:
                # не выполняем задачу, просто логируем, что не дождались условия и выводим время
                print(f"escaping by timer with {threading.current_thread().name=}, {perf_counter() - start}")

    def run(self):
        self.make_work()


def task():
    print(f"working task with {threading.current_thread().name=}")


_count = count(1)
condition = threading.Condition()


def permission():
    n = next(_count)  # считаем сколько раз вызывалась функция permission
    print(f"calling permission {n} with {threading.current_thread().name=}")
    return False


tw_1 = TestWorker(task=task, permission=permission, condition=condition).start()

tw_2 = TestWorker(task=task, permission=permission, condition=condition).start()