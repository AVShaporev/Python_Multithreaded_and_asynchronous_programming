from threading import Thread, Timer
import requests


sources = ["https://ya.ru",
           "https://www.bing.com",
           "https://www.google.ru",
           "https://www.yahoo.com",
           "https://mail.ru"]

def get_request_header(url: str) -> dict:
    return requests.get(url).headers

class GetHeaders(Thread):
    def __init__(self, url: str):
        super().__init__()
        self.url = url
        self.url_headers = None
    
    def run(self):
        global get_request_header
        self.url_headers = dict({self.url: get_request_header(self.url)})


my_threads = []
results = {}

for url in sources:
    my_threads.append(GetHeaders(url))

for thread in my_threads:
    thread.daemon = True
    thread.start()

for thread in my_threads:
    thread.join(2)

for thread in my_threads:
    results.update(thread.url_headers)

print(results)