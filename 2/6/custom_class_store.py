import threading

class LocalContexts(threading.local):
    def __init__(self):
        super().__init__()
        self._contexts = []

    def append(self, item):
        self._contexts.append(item)

    def pop(self):
        return self._contexts.pop()