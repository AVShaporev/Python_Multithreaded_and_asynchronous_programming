# простейший пример для закрепления:


from concurrent.futures import ThreadPoolExecutor
import time
import threading


def inition(*args):
    print(f"start initializer with {threading.current_thread().name} with {args=}")


def my_function(num):
    print(f"Start_processing_{num}_with_{threading.current_thread().name}")
    time.sleep(num)
    print(f"Finish_processing_{num}_with_{threading.current_thread().name}")
    return num * 2


with ThreadPoolExecutor(max_workers=2, initializer=inition, initargs=(112, 911), thread_name_prefix="T") as executor:
    results = executor.map(my_function, [1, 2, 3, 4, 5])
    for result in results:
        print(result)


'''
В этом примере мы создаем пул из двух потоков, используя конструкцию
with ThreadPoolExecutor(max_workers=2, initializer=inition, initargs=(112, 911), thread_name_prefix="T") as executor
указывая все аргументы: количество рабочих потоков, функцию инициализации, аргументы для нее и префикс имени рабочих потоков.
Затем мы отправляем на выполнение 5 задач, каждая из которых представляет собой вызов функции my_function() с числовым аргументом num, которое будет передаваться в функцию из списка [1, 2, 3, 4, 5].
Функция my_function() просто выводит сообщение о начале и завершении обработки, а затем возвращает удвоенное значение аргумента num. Обработку эмулируем функцией sleep().
Мы используем метод executor.map() для отправки всех задач на выполнение в пуле потоков и получения результата. Метод map() возвращает итератор, который генерирует результаты выполнения функции для каждого элемента входной последовательности. Затем мы выводим каждый результат с помощью цикла for.
Перед началом задачи каждый рабочий поток единожды вызывает функцию инициализации.
Создание ThreadPoolExecutor через контекстный менеджер (with-блок) гарантирует, что после выполнения всех задач, пул потоков будет корректно закрыт и все ресурсы будут освобождены. Использование контекстного менеджера гарантирует, что мы не забудем закрыть пул потоков, даже если произойдет исключение в процессе выполнения задач. После завершения блока with менеджер контекста автоматически вызывает метод shutdown() для ThreadPoolExecutor, который корректно закрывает пул потоков и освобождает все связанные с ним ресурсы.
'''

# start initializer with T_0 with args=(112, 911)
# Start_processing_1_with_T_0start initializer with T_1 with args=(112, 911)

# Start_processing_2_with_T_1
# Finish_processing_1_with_T_0
# 2Start_processing_3_with_T_0

# Finish_processing_2_with_T_1
# Start_processing_4_with_T_14

# Finish_processing_3_with_T_0
# Start_processing_5_with_T_0
# 6
# Finish_processing_4_with_T_1
# 8
# Finish_processing_5_with_T_0
# 10
