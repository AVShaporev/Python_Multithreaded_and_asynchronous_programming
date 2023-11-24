from threading import Thread
import requests


class GetHeaders(Thread):
    def __init__(self, url: str):
        super().__init__()
        self.url = url
        self.url_headers = None
    
    def run(self):
        global get_request_header
        self.url_headers = dict({self.url: get_request_header(self.url)})

