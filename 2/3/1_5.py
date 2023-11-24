import threading
from typing import Callable

# Исправьте ошибки в классе
class MyThread(threading.Thread):
    def __init__(self, msg_error: str = "error", task: Callable = None):
        super().__init__()
        self.msg_error = msg_error
        self.task = task

    def start(self) -> None:
        try:
            self.start(self.task())
        except Exception as err:
            print(self.msg_error)