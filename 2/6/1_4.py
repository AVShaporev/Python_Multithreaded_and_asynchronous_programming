import threading

stor = threading.local()
stor.a = 100


def test():
    stor.a = 0  # в локальном хранилище создаем свой собственный атрибут а отличный от атрибута главного потока
    print(f"{threading.current_thread().name}, {stor.a=}")
    print(stor.__dict__)
    print(stor)


thr_1 = threading.Thread(target=test, name="T1")
thr_1.start()
print(f"{threading.current_thread().name}, {stor.a=}")
print(stor.__dict__)
print(stor)

# T1, stor.a=0
# {'a': 0}
# <_thread._local object at 0x0000011162CD8900>
# MainThread, stor.a=100
# {'a': 100}
# <_thread._local object at 0x0000011162CD8900>