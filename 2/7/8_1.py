import threading
from time import sleep

cond = threading.Condition(lock=threading.Lock())  # создание объекта блокировки с условием


# здесь влзможно бесконечное зависаение
# def test():
#     name = threading.current_thread().name
#     print(f"{name} starting test")
#     with cond:  # защищаем блокировкой 
#         print(f"{name} executing crit.sector") # выполняем сразу
#         cond.wait()
#         print(f"{name} executing after wait()") # выполняем после условия

# здесь зависание так же возможно
# def test():
#     name = threading.current_thread().name
#     print(f"{name} starting test")
#     with cond:  # защищаем блокировкой 
#         cond.wait()  # выполняем все сразу одним куском после ожидания
#         print(f"{name} executing crit.sector")
#         print(f"{name} executing after wait()")

# здесь зависание избегается
def test():
    name = threading.current_thread().name
    print(f"{name} starting test")
    with cond:
        cond.wait()
        print(f"{name} executing crit.sector 1")
        cond.wait()
        print(f"{name} executing crit.sector 2")


th_1 = threading.Thread(target=test, name="T1")
th_2 = threading.Thread(target=test, name="T2")
th_1.start()
th_2.start()

with cond:
    print("main calling notify")
    cond.notify_all() 

sleep(0.1)  # специально задерживаемся перед вторым вызовом notify
with cond:
    print("main calling notify again")
    cond.notify_all()

th_1.join()
th_2.join()
print("END")