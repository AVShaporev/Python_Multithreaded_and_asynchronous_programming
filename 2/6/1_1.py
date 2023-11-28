import threading

a = 100

def test():
    print(f"{threading.current_thread().name}, {a=}")


thr_1 = threading.Thread(target=test, name="T1")
thr_2 = threading.Thread(target=test, name="T2")
thr_1.start()
thr_2.start()
print(f"{threading.current_thread().name}, {a=}")

# T1, a=100
# T2, a=100
# MainThread, a=100