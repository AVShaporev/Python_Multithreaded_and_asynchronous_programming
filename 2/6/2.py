from threading import Thread, local

# где-то определен stor_local = local()


def make_msg(stor_local: local):
    authentication = hasattr(stor_local, "authentication")
    fileno = None
    date_and_time = None
    if hasattr(stor_local, "fileno"):
        fileno = stor_local.fileno
    if hasattr(stor_local, "dt"):
        date_and_time = stor_local.dt
    return f"{authentication=}, {fileno=}, {date_and_time=}"