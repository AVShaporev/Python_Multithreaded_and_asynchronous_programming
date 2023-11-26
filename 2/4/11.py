'''
Перед Вами код, написанный стажером. Позже он будет использоваться как часть
 общего решения над которым работает команда, но сначала его нужно исправить. 
 Найдите все ошибки и исправьте код.

Стажер должен был реализовать простую модель: два потребителя - один 
производитель. Поток - производитель должен получать элемент из источника 
(функция - генератор get_obj()) и если элемент проходит проверку, то отправлять 
его на обработку. Обработка выполняется двумя демоническими потоками - потребителями.
 Проверка должна выполняться функцией is_valid(). Функция принимает элемент и возвращает 
 True или False. Если элемент не проходит проверку (is_valid возвращает False), 
 производитель добавляет элемент в очередь none_valid_queue. Два потока - потребителя 
 должны получать элементы из очереди валидных элементов и обрабатывать их, запуская 
 функцию обработчика handler(). Функция handler в качестве аргумента принимает один 
 элемент и выполняется не дольше чем 0.5 секунды в нормальных условиях. Для контроля 
 выполнения этого условия в решении должны были применяться таймауты.
'''

from queue import Queue
from threading import Thread

valid_queue = Queue()
none_valid_queue = Queue()


def task():
    global valid_queue
    while valid_queue.not_empty:
        elem = valid_queue.get()
        handler(elem)


t1 = Thread(target=task, daemon=True)
t2 = Thread(target=task, daemon=True)



def main():
    global get_obj
    global is_valid
    global valid_queue
    global none_valid_queue
    for elem in get_obj():
        if is_valid(elem):
            valid_queue.put(elem)
        else:
            none_valid_queue.put(elem)


main_th = Thread(target=main)

main_th.start()
t1.start()
t2.start()


main_th.join()
t1.join(0.5)
t2.join(0.5)