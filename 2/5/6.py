'''
Заказчик захотел функционал, позволяющий выявлять незанятость своих таможенных инспекторов. Если инспектор не получает на проверку новую таможенную декларацию в течении какого-то времени, об этом следует известить руководство. По результатам таких логов, например, можно оптимизировать кадровый состав.

К счастью, решение команды построить демонстрационную модель на основе очередей, позволяет довольно просто внедрить этот новый функционал. Ваша задача - переписать целевую функцию потребителя так, чтобы в случае неполучения декларации из очереди за установленное время (очередь пуста - работы нет), поток выводил сообщение и завершал свою работу.

Итак, Ваша задача:

1. Переписать вашу целевую функцию с прошлого задания так, чтобы в случае неполучения за заданное время (параметр функции t_wait, тип float) нового объекта - декларации из очереди, выводилось сообщение в формате:
Empty <datetime> thread = <name>
где <datetime>- дата и время формирования сообщения (используйте функцию datetime.now() билиотеки datetime)
<name> - имя потока - потребителя
например
Empty 2023-05-12 15:00:32.071063 thread = insp_1
и после этого поток - потребитель завершал свою работу.
Если же объект получен - то выводить id этого объекта простым принтом.
2. Для демонстрации создайте и запустите один поток-потребитель этой функции с параметром t_wait. Имя потока - потребителя "insp_1".
Тестирующая система проверяет поведение решение с разными параметрами t_wait. Очереди, декларации, поток - производитель и т.д. реализованы в тестирующей системе под старыми именами. Значение задаваемого параметра t_wait будет определено в тестирующей системе.
'''

import queue
import threading
from queue import PriorityQueue
from  datetime import datetime
from time import time
# from time import perf_counter as pc

class CCD(PriorityQueue):
    def __init__(self, dict_inf):
        super().__init__()
        self.cat = dict_inf['cat']
        self.union = dict_inf['union']
        self.cargo = dict_inf['cargo']
        self.id = dict_inf['id']

    def __lt__(self, other):
        if not isinstance(other, type(self)):
            raise NotImplemented
        cat_self = True
        cat_other = True

        if self.cat in ("0201", "0202", "0203", "0204", "0205", "0206", "0207", "0208", "0209"):
            cat_self = True
        else:
            cat_self = False

        if other.cat in ("0201", "0202", "0203", "0204", "0205", "0206", "0207", "0208", "0209"):
            cat_other = True
        else:
            cat_other = False

        return (self.union, cat_self, -self.id) > (other.union, cat_other, -other.id)

    def __repr__(self):
        return f'{self.union}, {self.cat}, {self.id}, {self.cargo}'
    

d1 = {"cat": "0210", "union": True, "cargo": {"stew", 2}, "id": 1}
d2 = {"cat": "0208", "union": True, "cargo": {"liver", 1.78}, "id": 2}
d3 = {"cat": "0208", "union": True, "cargo": {"liver", 56}, "id": 3}
d4 = {"cat": "0209", "union": False, "cargo": {"pork fat", 100}, "id": 4}
d5 = {"cat": "87", "union": False, "cargo": {"bombardier", 1}, "id": 5}


products = [CCD(d1), CCD(d2), CCD(d3), CCD(d4), CCD(d5), None]

t_wait = 0.0001


def handler(item):
    return item.id % 2 > 0

# создайте две очереди
main_queue = queue.PriorityQueue(maxsize=30)
sup_queue = queue.Queue()

# напишите функцию производителя
def producer():
    for item in products:
        if item is None:
            break
        else:
            if not main_queue.full():
                main_queue.put(item)
            else:
                sup_queue.put(item)

# перепишите целевую функцию предыдущего задания с учетом нового условия работы
def consumer(t_wait: float):

    while True:
        try:
            i = main_queue.get(timeout=t_wait)
        except:
            print(f"Empty {datetime.now()} thread = {threading.current_thread().name}")
            return
        else:
            print(i.id)

        main_queue.task_done()

# создайте и запустите поток - производитель, дождитесь его завершения
prod_0 = threading.Thread(target=producer, name='prod_0')
prod_0.start()

# создайте и запустите потоки - инспекторы
insp_1 = threading.Thread(target=consumer, args=(t_wait, ), name='insp_1', daemon=True)

# после завершения обработки всех деклараций из очереди,
prod_0.join()
insp_1.start()
# insp_1.join()


main_queue.join()


# переместите в главную очередь все декларации из вспомог. очереди.
while not sup_queue.empty():
     main_queue.put(sup_queue.get())
