import threading


class PrintThread(threading.Thread):  # наследуем оригинальный класс Thread

    def __init__(self, text):
        super().__init__()
        self.text = text

    def run(self):
        print(self.text)


my_thread = PrintThread("Text")  # Создаем объект кастомного потока
thread = threading.Thread()      # Создаем объект потока стандарным конструктором
print(my_thread.__dict__)        # Смотрим доступные методы и атрибуты обоих потоков
print(thread.__dict__)