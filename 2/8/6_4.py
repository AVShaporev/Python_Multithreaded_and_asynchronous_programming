'''
Если необходимо организовать перезапуск отдельного этапа в целевой задаче, можно использовать флаги успешного завершения этапов, а саму целевую задачу упаковывать в циклы выполнения этапов с успешным и неуспешным выходом из каждого цикла - этапа. Тогда метод reset можно вызывать в finally:
'''

import threading
from time import sleep

def finalizer():
    print(f"last thread {threading.current_thread().name} stage done")


barrier = threading.Barrier(4, action=finalizer)


def multi_stage_task(t):
    stage1_completed = False
    stage2_completed = False

    while True:
        if not stage1_completed:
            try:
                print(f"Stage 1 in {threading.current_thread().name} starting")
                sleep(t)  # эмуляция работы
                barrier.wait(2)
                print(f"Stage 1 in {threading.current_thread().name} continuing")
            except threading.BrokenBarrierError:
                print(f"{threading.current_thread().name} encountered a broken barrier. Retrying stage 1...")
                t = 1   #  Операции, позволяющие выполнить повтор успешно (в нашем примере уменьшаем t)
                continue
            else:
                stage1_completed = True
            finally:
                barrier.reset()

        if not stage2_completed:
            try:
                print(f"Stage 2 in {threading.current_thread().name} starting")
                sleep(t)  # эмуляция работы
                barrier.wait(2)
                print(f"Stage 2 in {threading.current_thread().name} continuing")
            except threading.BrokenBarrierError:
                print(f"{threading.current_thread().name} encountered a broken barrier. Retrying stage 1...")
                t = 1   #  Операции, позволяющие выполнить повтор успешно (в нашем примере уменьшаем t)
                continue
            else:
                stage2_completed = True
            finally:
                barrier.reset()

thr = [threading.Thread(target=multi_stage_task, args=(i, )) for i in range(4)]
for t in thr:
    t.start()

sleep(10)
print(barrier.n_waiting)

# Stage 1 in Thread-1 (multi_stage_task) starting
# Stage 1 in Thread-2 (multi_stage_task) startingStage 1 in Thread-3 (multi_stage_task) starting

# Stage 1 in Thread-4 (multi_stage_task) starting
# Thread-1 (multi_stage_task) encountered a broken barrier. Retrying stage 1...Thread-2 (multi_stage_task) encountered a broken barrier. Retrying stage 
# 1...

# Stage 1 in Thread-2 (multi_stage_task) starting
# Stage 1 in Thread-1 (multi_stage_task) starting
# last thread Thread-1 (multi_stage_task) stage done
# Stage 1 in Thread-1 (multi_stage_task) continuingStage 1 in Thread-2 (multi_stage_task) continuingStage 1 in Thread-4 (multi_stage_task) continuingStage 1 in Thread-3 (multi_stage_task) continuing



# Stage 2 in Thread-1 (multi_stage_task) startingStage 2 in Thread-2 (multi_stage_task) startingStage 2 in Thread-4 (multi_stage_task) startingStage 2 in Thread-3 (multi_stage_task) starting



# Thread-2 (multi_stage_task) encountered a broken barrier. Retrying stage 1...Thread-4 (multi_stage_task) encountered a broken barrier. Retrying stage 
# 1...
# Thread-1 (multi_stage_task) encountered a broken barrier. Retrying stage 1...
# Thread-3 (multi_stage_task) encountered a broken barrier. Retrying stage 1...Stage 2 in Thread-4 (multi_stage_task) starting
# Stage 2 in Thread-1 (multi_stage_task) starting


# Stage 2 in Thread-2 (multi_stage_task) startingStage 2 in Thread-3 (multi_stage_task) starting

# last thread Thread-1 (multi_stage_task) stage done
# Stage 2 in Thread-1 (multi_stage_task) continuingStage 2 in Thread-2 (multi_stage_task) continuing
# Stage 2 in Thread-3 (multi_stage_task) continuing
# Stage 2 in Thread-4 (multi_stage_task) continuing

# 0