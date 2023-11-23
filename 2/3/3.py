import threading
from typing import Callable

# Создайте класс SimpleThread
class SimpleThread(threading.Thread):
    def __init__(self, function: Callable, data: Any):
        super().__init__()
        self.function = function
        self.data = data
        
    def run(self):
        print(self.function(self.data))