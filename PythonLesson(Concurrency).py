# *lock
import math
# *race condition
#
# import threading
# counter  = 0
# def increment():
#     global counter
#
#     for _ in range(100_000):
#         counter+=1
#
# threads = [
#     threading.Thread(target=increment),
#     threading.Thread(target=increment)
# ]
# for thread in threads:
#     thread.start()
#
# for thread in threads:
#     thread.join()
#
# print(counter)

# *protected version
# import threading
#
# counter = 0
# lock = threading.Lock()
#
# def increment():
#     global counter
#
#     for _ in range(100_000):
#         with lock:
#             counter +=1
# threads = [
#     threading.Thread(target=increment),
#     threading.Thread(target=increment)
# ]
#
# for thread in threads:
#     thread.start()
#
# for thread in threads:
#     thread.join()
#
# print(counter)

# *Daemon Threads
#
# A thread can be created as a daemon:
#
# thread = threading.Thread(
#     target=task,
#     daemon=True
# )
#
# Daemon threads are generally intended for background work that should not keep the
# Python process alive when all non-daemon threads have finished.


# *Thread pools
# *1st approach
from concurrent.futures import ThreadPoolExecutor
# *import time
#
# def download(file_name):
#     time.sleep(2)
#     return f"{file_name} downloaded"
#
# with ThreadPoolExecutor(max_workers=3) as executor:
#     results = executor.map(
#         download,
#         ["a.zip","b.zip","c.zip"]
#     )
#
#     for result in results:
#         print(result)

# *2nd approach
def calculate(x):
    return math.pow(x,2)

with ThreadPoolExecutor(max_workers=3) as executor:
    future = executor.submit(calculate,10)

    result = future.result()

print(result)

