import requests
import threading
from time import perf_counter


# sources = ["https://ya.ru",
#            "https://www.bing.com",
#            "https://www.google.ru",
#            "https://www.yahoo.com",
#            "https://mail.ru"]

# headers_stor = {}  # Храним здесь заголовки
# start = perf_counter()
# sum_ex_time = 0


# for source in sources:
#     start_tmp = perf_counter()
#     headers_stor[source] = requests.get(source).headers  # получаем заголовки и формируем словарь
#     delta = perf_counter() - start_tmp
#     print(source, delta)
#     sum_ex_time += delta

# print(f"completed in {perf_counter()-start} seconds")  # Считаем общее время выполнения всех запросов
# print(sum_ex_time)  # Показываем то, что общее время работы является простой суммой каждого запроса по отдельности
# print(*headers_stor.items(), sep="\n")  # Выводим наши заголовки


sources = ["https://ya.ru",
           "https://www.bing.com",
           "https://www.google.ru",
           "https://www.yahoo.com",
           "https://mail.ru"]

headers_stor = {}  # Храним здесь заголовки
start = perf_counter()
sum_ex_time = 0


def get_header(source):
    headers_stor[source] = requests.get(source).headers
    



task = threading
threads = []

for source in sources:
    thread = task.Thread(target=get_header, args=(source,))  # получаем заголовки и формируем словарь
    thread.start()
    threads.append(thread)



for i in threads:
    start_tmp = perf_counter()
    i.join()
    delta = perf_counter() - start_tmp
    print(source, delta)
    sum_ex_time += delta

print(f"completed in {perf_counter()-start} seconds")  # Считаем общее время выполнения всех запросов
print(sum_ex_time)  # Показываем то, что общее время работы является простой суммой каждого запроса по отдельности
print(*headers_stor)  # Выводим наши заголовки