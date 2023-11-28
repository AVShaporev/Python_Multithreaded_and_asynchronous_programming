import threading

stor = threading.local() # Создаем локальное хранилище Main потока
stor.a = 100  # Создаем атрибут хранилища и передаем ему значение
print(stor.__dict__)

# {'a': 100}