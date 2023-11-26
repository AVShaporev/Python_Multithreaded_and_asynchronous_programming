import threading
import queue
from time import sleep

queue = queue.PriorityQueue(60)  # Очередь с приоритетом, ограничим размер.
account = 0  #  Сумма на расчетном счете. Все платежные поручения выполняются с этим счетом.


def producer(t: int | float, file: str):
    with open(file) as file:
        for line in file:
            priority, amount, assignment = line.split()  # Кажая строка это приоритет, сумма, поручение через пробел
            queue.put((int(priority), int(amount), assignment))
            print(f"{threading.current_thread().name}\tput\t->\t({line.strip()})\tQueue size = {queue.qsize()}")
            sleep(t)


def consumer(t: int | float):
    global account  # все потоки работают с единым расчетным счетом
    while True:
        payment = queue.get()  # получаем поручение
        priority, amount, assignment = payment
        print(f"{threading.current_thread().name}\t<-\tget\t{payment}\tQueue size = {queue.qsize()}")
        # sleep(t)
        if assignment == "receipt":  # в зависимости от операции поручения выполняется либо зачисление, либо списание
            account += amount
        else:
            account -= amount
        queue.task_done()  # задание помечается выполненным


thread_1 = threading.Thread(target=producer, args=(0.1, r"C:\Users\avsha\Dev\Python_Multithreaded_and_asynchronous_programming\2\5\2\my_payment_orders_1.txt"), name="producer_1")
thread_2 = threading.Thread(target=producer, args=(0.3, r"C:\Users\avsha\Dev\Python_Multithreaded_and_asynchronous_programming\2\5\2\my_payment_orders_2.txt"), name="producer_2")
thread_3 = threading.Thread(target=consumer, args=(0.3, ), name="consumer_1", daemon=True)
thread_4 = threading.Thread(target=consumer, args=(1.5, ), name="consumer_2", daemon=True)
thread_5 = threading.Thread(target=consumer, args=(2, ), name="consumer_3", daemon=True)
thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()
thread_5.start()


thread_1.join()  # ждем завершения потока производителя №1
thread_2.join()  # ждем завершения потока производителя №2

queue.join()  # дожидаемся когда все поручения будут исполнены

print(f"{account=}")  # печатаем общее состояние счета
print("END MAIN")