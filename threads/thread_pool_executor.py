from concurrent.futures import ThreadPoolExecutor
import time

def task(n):
    print(f"Task {n} started")
    time.sleep(2)
    print(f"Task {n} finished")


with ThreadPoolExecutor(max_workers=3) as executor:
    for i in range(5):
        executor.submit(task, i)
