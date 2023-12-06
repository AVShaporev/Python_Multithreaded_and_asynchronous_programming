# from threading import Thread, local
import threading

# где-то определен stor_local = local()
stor_local = threading.local()


def make_msg():
    if threading.current_thread().name == 'Thread-1 (make_msg)':
        stor_local.authentication = 'Accses'
    if threading.current_thread().name == 'Thread-2 (make_msg)':
        stor_local.authentication = 'NoAccses'
    if threading.current_thread().name == 'Thread-3 (make_msg)':
        stor_local.authentication = 'NoAccses!!!!!'    
    authentication = hasattr(stor_local, "authentication")
    fileno = None
    date_and_time = None
    if hasattr(stor_local, "fileno"):
        fileno = stor_local.fileno
    if hasattr(stor_local, "dt"):
        date_and_time = stor_local.dt
    print(f"{stor_local.authentication=}, {fileno=}, {date_and_time=}")


my_thread1 = threading.Thread(target=make_msg, daemon=True)
my_thread2 = threading.Thread(target=make_msg, daemon=True)
my_thread3 = threading.Thread(target=make_msg, daemon=True)




my_thread1.start()
my_thread2.start()
my_thread3.start()

my_thread1.join()
my_thread2.join()
my_thread3.join()
