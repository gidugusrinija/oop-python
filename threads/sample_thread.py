import threading
import time
import requests


def get_data(url):
    print("Task 2 started")
    print(threading.current_thread().name)
    requests.get(url)
    print("Task 2 finished")


def task(n):
    print(f"Task {n} started")
    print(threading.current_thread().name)
    time.sleep(3)
    print(f"Task {n} finished")


print(threading.current_thread().name)
t1 = threading.Thread(target=task, name="Thread1", args=(1,))
t2 = threading.Thread(target=get_data, name="Thread2", args=("https://www.linkedin.com/in/gidugu-srinija",))

t2.start()
print(threading.current_thread().name)
t1.start()
print(threading.current_thread().name)
t1.join()

t2.join()
print(threading.current_thread().name)
