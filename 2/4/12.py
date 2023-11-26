'''
Усложним задачу из 10 шага. Теперь функция генератор get_obj() 
и функция is_prim() могут ненадолго "подвисать". Генератор не 
мгновенно возвращает очередной элемент, а функция проверки не 
мгновенно возвращает результат. Но гарантируется, что в случае 
серьезных проблем генератор возвращает значение None. После 
этого запрашивать следующее значение у генератора не нужно, это 
может привести к сбоям, ошибкам или зависанию. А функция is_prim() 
гарантированно выполняется не дольше чем 0.2 секунды.

Ваша задача осталась прежней: создать и заполнить две очереди, 
только сделать это нужно двумя потоками для улучшения 
производительности и отзывчивости. Поэтому создайте два дочерних 
потока - сортировщика, каждый будет складывать в обе очереди в 
зависимости от результата работы функции is_prim().

Тестирующая система проверит общее время выполнения программы, 
содержимое обеих очередей prim_queue, sub_queue.

Подумайте как организовать передачу объектов из функции генератора 
в два потока - сортировщика. Как остановить работу дочерних 
потоков и всей программы в случае получения значения None, но в 
то же время все-таки дождаться выполнения функции is_prim() для 
предыдущего (до None) значения, полученного от генератора.
'''

from queue import Queue
from threading import Thread
from time import sleep


class iter_obj:
    def __init__(self, my_lst: list):
        self._lst = my_lst
        self.higth = len(self._lst)
        self.low = 0


    def __iter__(self):
        return self
    
    def __next__(self):
        self.low += 1
        if  self.low <= self.higth:
            i = self._lst[-self.low]
            return i
        else:
            raise StopIteration
        
    def __call__(self):
        self.low += 1
        if  self.low <= self.higth:
            i = self._lst[-self.low]
            return i
        else:
            raise StopIteration        
    
    def __str__(self):
        return f'{self._lst}'
        

get_obj = iter_obj([None, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


def is_prim(num):
    sleep(0.2)
    if num is not None:
        return num % 2 == 0
    else:
        return False


time_oj = float(input('Ввести время выполнения потока: '))

prim_queue = Queue()
sub_queue = Queue()
temp_queue = Queue()
my_flag = True

def producer():
    for i in get_obj:
        print(i)
        if i is None:
            break
        else:
            temp_queue.put(i)
        

def consumer():
    while True:

        global prim_queue
        global sub_queue
        global temp_queue

        i = temp_queue.get()

        if is_prim(i):
            prim_queue.put(i)
        else:
            sub_queue.put(i)


th_producer = Thread(target=producer)
consumer1 = Thread(target=consumer, daemon=True)
consumer2 = Thread(target=consumer, daemon=True)


consumer1.start()
consumer2.start()

th_producer.start()
th_producer.join()



consumer1.join(time_oj)
consumer2.join(time_oj)

print(f'{time_oj=}')

while not prim_queue.empty():
    print(prim_queue.get(), end=' ')

print()

while not sub_queue.empty():
    print(sub_queue.get(), end=' ')