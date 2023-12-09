import threading
import time

# _bl, _tm, _vl = True, 0, 0
'''
thread id = 5116 print 0, acquire=False, value= 0
thread id = 5412 print 1, acquire=False, value= 0  
thread id = 5260 print 2, acquire=False, value= 0  
thread id = 11508 print 3, acquire=False, value= 0 
thread id = 13680 print 4, acquire=False, value= 0 
thread id = 12124 print 5, acquire=False, value= 0 
thread id = 412 print 6, acquire=False, value= 0   
thread id = 9100 print 7, acquire=False, value= 0  
thread id = 2448 print 8, acquire=False, value= 0  
thread id = 5792 print 9, acquire=False, value= 0  
thread id = 9500 print 10, acquire=False, value= 0 
thread id = 3184 print 11, acquire=False, value= 0 
thread id = 5264 print 12, acquire=False, value= 0 
thread id = 2224 print 13, acquire=False, value= 0 
thread id = 10012 print 14, acquire=False, value= 0
thread id = 7748 print 15, acquire=False, value= 0 
thread id = 9288 print 16, acquire=False, value= 0
thread id = 7036 print 17, acquire=False, value= 0
thread id = 14584 print 18, acquire=False, value= 0
thread id = 13308 print 19, acquire=False, value= 0
20
'''


# _bl, _tm, _vl = False, 0, 0
'''
...
: ValueError
ValueError: can't specify timeout for non-blocking acquirecan't specify timeout for non-blocking acquire: 

can't specify timeout for non-blocking acquire
'''


# _bl, _tm, _vl = False, None, 1
'''
thread id = 2464 print 0, acquire=True, value= 0
thread id = 252 print 1, acquire=False, value= 0thread id = 4972 print 2, acquire=False, value= 0
thread id = 7980 print 3, acquire=False, value= 0
thread id = 11212 print 4, acquire=False, value= 0
thread id = 6548 print 5, acquire=False, value= 0
thread id = 14700 print 6, acquire=False, value= 0thread id = 14772 print 7, acquire=False, value= 0


thread id = 620 print 8, acquire=False, value= 0thread id = 10596 print 9, acquire=False, value= 0

thread id = 1352 print 10, acquire=False, value= 0thread id = 12852 print 11, acquire=False, value= 0

thread id = 1464 print 12, acquire=False, value= 0thread id = 10752 print 13, acquire=False, value= 0

thread id = 5244 print 14, acquire=False, value= 0
thread id = 14284 print 15, acquire=False, value= 0
thread id = 8848 print 16, acquire=False, value= 0
thread id = 1396 print 17, acquire=False, value= 0
thread id = 5468 print 18, acquire=False, value= 0thread id = 5860 print 19, acquire=False, value= 0

20
'''



# _bl, _tm, _vl = True, 2.5, 2
'''
thread id = 12036 print 0, acquire=True, value= 1
thread id = 13056 print 1, acquire=True, value= 0
thread id = 2952 print 2, acquire=True, value= 0thread id = 5676 print 3, acquire=True, value= 0

thread id = 11812 print 4, acquire=True, value= 1thread id = 11836 print 5, acquire=True, value= 0

thread id = 14620 print 8, acquire=False, value= 0thread id = 11344 print 12, acquire=False, value= 0thread id = 6212 print 13, acquire=False, value= 
0thread id = 11424 print 14, acquire=False, value= 0
thread id = 11624 print 6, acquire=False, value= 0

thread id = 10520 print 11, acquire=False, value= 0thread id = 13236 print 15, acquire=False, value= 0
thread id = 13996 print 7, acquire=False, value= 0
thread id = 5240 print 10, acquire=False, value= 0thread id = 7880 print 9, acquire=False, value= 0




thread id = 8556 print 16, acquire=False, value= 0thread id = 7868 print 17, acquire=False, value= 0thread id = 4844 print 18, acquire=False, value= 0thread id = 11980 print 19, acquire=False, value= 0



16
'''



# _bl, _tm, _vl = True, None, 10
'''
thread id = 7684 print 0, acquire=True, value= 9
thread id = 11628 print 1, acquire=True, value= 8
thread id = 14436 print 2, acquire=True, value= 7thread id = 13248 print 3, acquire=True, value= 6

thread id = 1056 print 4, acquire=True, value= 5thread id = 13928 print 5, acquire=True, value= 4

thread id = 7892 print 6, acquire=True, value= 3
thread id = 11548 print 7, acquire=True, value= 2thread id = 15276 print 8, acquire=True, value= 1

thread id = 9196 print 9, acquire=True, value= 0
thread id = 14736 print 10, acquire=True, value= 0thread id = 4776 print 11, acquire=True, value= 0

thread id = 616 print 12, acquire=True, value= 7thread id = 14260 print 13, acquire=True, value= 6thread id = 15248 print 15, acquire=True, value= 5thread id = 13148 print 18, acquire=True, value= 4
thread id = 14108 print 16, acquire=True, value= 3
thread id = 7408 print 14, acquire=True, value= 2thread id = 9200 print 19, acquire=True, value= 1thread id = 8648 print 17, acquire=True, value= 0   





10
'''



_bl, _tm, _vl = True, 0, 10
'''
thread id = 13904 print 0, acquire=True, value= 9
thread id = 4668 print 1, acquire=True, value= 8
thread id = 5212 print 2, acquire=True, value= 7thread id = 14524 print 3, acquire=True, value= 6

thread id = 10176 print 4, acquire=True, value= 5thread id = 10100 print 5, acquire=True, value= 4

thread id = 7396 print 6, acquire=True, value= 3thread id = 5520 print 7, acquire=True, value= 2

thread id = 7672 print 8, acquire=True, value= 1
thread id = 8976 print 9, acquire=True, value= 0thread id = 3400 print 10, acquire=False, value= 0

thread id = 9124 print 11, acquire=False, value= 0
thread id = 13212 print 12, acquire=False, value= 0
thread id = 10432 print 13, acquire=False, value= 0
thread id = 8156 print 14, acquire=False, value= 0
thread id = 14020 print 15, acquire=False, value= 0
thread id = 4032 print 16, acquire=False, value= 0
thread id = 14796 print 17, acquire=False, value= 0
thread id = 14632 print 18, acquire=False, value= 0
thread id = 12296 print 19, acquire=False, value= 0
20
'''






def task(sema: threading.Semaphore, text):
    s = sema.acquire(blocking=_bl, timeout=_tm)
    print(f"thread id = {threading.current_thread().ident} print {text}, acquire={s}, value= {sema._value}")
    time.sleep(1)
    sema.release()


semaphore = threading.Semaphore(_vl)

thr = []
for i in range(20):
    thr.append(threading.Thread(target=task, args=(semaphore, i)))
for t in thr:
    t.start()

for t in thr:
    t.join()

print(semaphore._value)