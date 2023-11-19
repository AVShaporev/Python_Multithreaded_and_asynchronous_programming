from time import sleep

def user_interface():
    while True:
        sleep(0.2)
        print("-", end="")


def task():
    while True:
        sleep(0.61)
        print("*", end="")


import threading


# Ваше решение
tasks = [threading.Thread(target=user_interface), threading.Thread(target=task)]

for task in tasks:
    task.start()