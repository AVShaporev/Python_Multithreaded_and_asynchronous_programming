import threading

stor = threading.local() # Создаем объект локального хранилища
stor.a = 100  # Создаем атрибут, доступный только Main потоку и передаем ему значение


def test():
    try:
        print(f"{threading.current_thread().name}, {stor.a=}")  # Пытаемся получить доступ к перем. а
    except AttributeError as err:
        print(f"{threading.current_thread().name} {err}")


thr_1 = threading.Thread(target=test, name="T1")
thr_2 = threading.Thread(target=test, name="T2")
thr_1.start()
thr_2.start()
print(f"{threading.current_thread().name}, {stor.a=}")

# T1 '_thread._local' object has no attribute 'a'
# T2 '_thread._local' object has no attribute 'a'
# MainThread, stor.a=100