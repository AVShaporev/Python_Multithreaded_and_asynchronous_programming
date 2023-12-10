'''
В реальном использовании не стараются делать синхронизацию этапов в одной целевой задаче с повтором. В действительности стараются делать простую и прозрачную реализацию без лишних усложнений. Вот несколько примеров "боевой" реализации барьера в реальных проектах:

1. OpenStack: барьер используется в OpenStack для синхронизации потоков, выполняющих обработку запросов к API:
'''

import threading
from oslo_concurrency import barrier

class RequestHandlerThread(threading.Thread):
    def __init__(self, request, barrier):
        threading.Thread.__init__(self)
        self.request = request
        self.barrier = barrier

    def run(self):
        # Обработка запроса
        self.barrier.wait()

def process_requests(requests):
    num_threads = len(requests)
    request_barrier = barrier.Barrier(num_threads)

    threads = []
    for request in requests:
        thread = RequestHandlerThread(request, request_barrier)
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()