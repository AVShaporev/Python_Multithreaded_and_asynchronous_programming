from threading import Thread, local


def print_msg(stor_local):
    # if hasattr(stor_local, 'msg'):
    #     msg = stor_local.msg
    # else:
    #     msg = 'failure'

    # if hasattr(stor_local, 'fileno'):
    #     fileno = stor_local.fileno
    # else:
    #     fileno = 'failure'     

    # if hasattr(stor_local, 'permission'):
    #     permission = stor_local.permission
    # else:
    #     permission = 'guest'    

    msg = getattr(stor_local, "msg", "failure")
    fileno = getattr(stor_local, "fileno", "failure")
    permission = getattr(stor_local, "permission", "guest")      

    print(f"{msg}, {fileno=}, {permission}")