# def permission():
#     if stor_local.permission:
#         if not hasattr(permission, '_count'):  # инициализация значения
#             permission._count = {}
#         if not hasattr(permission, '_flag'):
#             permission._flag = True
#         if threading.current_thread().name in permission._count:
#             permission._count[threading.current_thread().name] += 1
#             if permission._count[threading.current_thread().name] == 2 and permission._flag:
#                 permission._flag = False
#                 return True
#         else:
#             permission._count[threading.current_thread().name] = 1        
#     return False


def permission():
    if stor_local.permission:
        if not hasattr(stor_local, '_count'):
            stor_local._count = 1
        else:
            return True
    return False