from threading import Thread, local

# где-то определен stor_local = local()
stor_local = local()


def make_msg(stor_local: local):
    authentication = hasattr(stor_local, "authentication")
    fileno = None
    date_and_time = None
    if hasattr(stor_local, "fileno"):
        fileno = stor_local.fileno
    if hasattr(stor_local, "dt"):
        date_and_time = stor_local.dt
    return f"{authentication=}, {fileno=}, {date_and_time=}"


my_thread1 = Thread(target=make_msg, args=(stor_local, ), daemon=True)
my_thread2 = Thread(target=make_msg, args=(stor_local, ), daemon=True)
my_thread3 = Thread(target=make_msg, args=(stor_local, ), daemon=True)

my_thread1.start()
my_thread2.start()
my_thread3.start()

my_thread1.join()
my_thread2.join()
my_thread3.join()
