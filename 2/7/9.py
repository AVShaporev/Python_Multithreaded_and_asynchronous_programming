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
    n = next(_count)
    thread_name = threading.current_thread().name
    print(f"calling permission {n} with {thread_name}")
    if not hasattr(permission, '_count'):  # инициализация значения
        permission._count = {}
    if not hasattr(permission, '_flag'):
        permission._flag = True
    if thread_name in permission._count:
        if permission._count[thread_name] == 2 and permission._flag:
            permission._flag = False
            return True
    else:
        permission._count[thread_name] = n
    return False


# def permission():
#     threadLocal = threading.local()
#     # print(f'1 - {threadLocal.name=}')
#     n = next(_count)
#     initialized = getattr(threadLocal, 'name', None)   #stor = threading.local() # Создаем объект локального хранилища
#     threadLocal.name = initialized
#     print(f'1 - {threadLocal.name=} {threading.current_thread().name=}')
#     if initialized is not None:
#         print(f'2 - {threadLocal.name=} {threading.current_thread().name=}')
#         print(f'{n=} {initialized=} True')       
#         return True
#     if n == 2:
#         print(f'3 - {threadLocal.name=} {threading.current_thread().name=}')
#         initialized = threadLocal.name
#         print(f'{n=} {threading.current_thread().name=} False')
#         return False
#     print(f'4 - {threadLocal.name=} {threading.current_thread().name=}')
#     print(f'{n=} False {threading.current_thread().name=}')
#     return False

# for _ in range(2):
#     my_thread = TestWorker(task=task, permission=permission, condition=condition)
#     my_thread.start()
#     my_thread.join()


tw_1 = TestWorker(task=task, permission=permission, condition=condition).start()
tw_2 = TestWorker(task=task, permission=permission, condition=condition).start()
tw_3 = TestWorker(task=task, permission=permission, condition=condition).start()
tw_4 = TestWorker(task=task, permission=permission, condition=condition).start()