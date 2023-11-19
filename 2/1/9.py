import threading


def get_request(link: str, ignor_err: bool = True, time_limit: int = 2) -> None:
    pass

# threading.Thread(target=get_request, args=(), kwargs={"link": "https://ufostalker.com"}).start()
# threading.Thread(target=get_request, args=("https://wordstat.yandex.ru", )).start()
# threading.Thread(target=get_request, args=["https://willrobotstakemyjob.com", 5, False]).start()
# threading.Thread(target=get_request, kwargs={"link": "http://worldbirthsanddeaths.com"}).start()
# threading.Thread(target=get_request, args=("https://weirdorconfusing.com"), kwargs={"time_limit": 3}).start()
# threading.Thread(target=get_request, args=["https://2ip.ru"]).start()
threading.Thread(target=get_request, args=("https://www.windows93.net", ), kwargs={"ignor_err": False}).start()