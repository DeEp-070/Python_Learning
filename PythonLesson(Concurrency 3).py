# *async programming

# * Synchronous
# result = get_data()
# print(result)

# *Asynchronous
#
# *Conceptually:
# start operation
#        ↓
# operation waits for I/O
#        ↓
# do other work
#        ↓
# operation becomes ready
#        ↓
# continue operation
#
# This is called cooperative concurrency.

#  *define async method
# * async def fetch_data():
#     return "data"
#
# # result = fetch_data() #doesn't immediately give you:  "data"
# # Instead, you get a coroutine object.
# # *Conceptually:
# #
# # fetch_data()
# #      ↓
# # Coroutine object
#
# # *await
# # To execute/await the coroutine from another async context:
# * async def main():
#     result = await fetch_data()
#     print(result)

# await means approximately:
# "Wait for this awaitable operation,
# but allow the event loop to work on other eligible tasks while this operation is suspended."

# * Actual example
# import asyncio
# async def fetch_data():
#     await asyncio.sleep(2)
#     return "Data"
#
# async def main():
#     result = await fetch_data()
#     print(result)
#
# asyncio.run(main())

# What Is a Coroutine?
# => A coroutine is a special function/execution object designed to be suspended and resumed.

#  * Creating concurrent tasks
# import asyncio
#
# async def task(name):
#     print(f"{name} started")
#
#     await asyncio.sleep(2)
#
#     print("Finished")
#
# async def main():
#     task1 = asyncio.create_task(task("A"))
#     task2 = asyncio.create_task(task("B"))
#     task3 = asyncio.create_task(task("C"))
#
#     await task1
#     await task2
#     await task3
#
# asyncio.run(main())

# * What Is an asyncio.Task?
# => A Task is essentially an asyncio-managed wrapper around a coroutine that
# schedules it for execution by the event loop.

# *The Event Loop
#
# The event loop is the central mechanism behind asyncio.
#
# Simplified:
#
#                  Event Loop
#                      │
#           ┌──────────┼──────────┐
#           ↓          ↓          ↓
#        Task A     Task B     Task C
#           │          │          │
#        waiting     running    waiting
#           │          │          │
#           └──────────┼──────────┘
#                      ↓
#                resume ready task
#
# The event loop repeatedly:-
# checks which tasks are ready
# runs them
# suspends tasks that reach an await
# waits for I/O/readiness
# resumes tasks when they can continue


# *Sequential Async vs Concurrent Async
# Sequential
# async def main():
#     a = await fetch_a()
#     b = await fetch_b()
#     c = await fetch_c()
#
# Conceptually:
#
# *A ███████
#         B ███████
#                 C ███████

#
# * Concurrent
# async def main():
#     task_a = asyncio.create_task(fetch_a())
#     task_b = asyncio.create_task(fetch_b())
#     task_c = asyncio.create_task(fetch_c())
#
#     a = await task_a
#     b = await task_b
#     c = await task_c
#
# *Conceptually:
#
# *A ███████
# *B ███████
# *C ███████
#
# provided the operations are genuinely independent and awaitable.


# *asyncio.gather()
# async def main():
#     results = await asyncio.gather(
#         fetch_a(),
#         fetch_b(),
#         fetch_c()
#     )
#
#     print(results)

# *Conceptually:
#
# *fetch_a ────────┐
# *fetch_b ────────┼──→ gather → results
# *fetch_c ────────┘
#

# * Example of three api calls
# import asyncio
#
# async def get_user():
#     await asyncio.sleep(2)
#     return "user"
#
# async def get_orders():
#     await asyncio.sleep(2)
#     return "Orders"
#
# async def get_recommendations():
#     await asyncio.sleep(2)
#     return "Recommendations"
#
# async def main():
#     user , order , recommendation = await asyncio.gather(
#          get_user(),
#          get_orders(),
#         get_recommendations()
#     )
#
#     print(user)
#     print(order)
#     print(recommendation)
#
# asyncio.run(main())


# *Task cancellation
# Tasks can be cancelled:
#
# task.cancel()
#
# The coroutine can receive cancellation at an appropriate cancellation point.
#
# Cancellation matters in real systems when:
#
# a client disconnects
# a request times out
# a service shuts down
# a parent task no longer needs the result

# * asyncio.lock
# import asyncio
#
# balance = 1000
# lock = asyncio.Lock()
#
# async def withdraw(amount):
#     global balance
#
#     async with lock:
#         if balance >= amount:
#             await asyncio.sleep(0.1)
#             balance -= amount
#             return  True
#         return False
#
# async def main():
#     task1,task2 = await asyncio.gather(
#         withdraw(5000),
#         withdraw(500)
#     )
#     print(task1)
#     print(task2)
#
# asyncio.run(main())


# * semaphore in async
# A lock allows:
# 1 task
#
# into a critical section.
# A semaphore allows a limited number of tasks.

# semaphore = asyncio.Semaphore(3)
#
# Then:
#
# async with semaphore:
#     await make_request()
#
# At most three tasks can enter that section simultaneously.
# import asyncio
#
# balance = 1000
# semaphore = asyncio.Semaphore(2)
#
# async def withdraw(amount):
#     global balance
#
#     async with semaphore:
#         if balance >= amount:
#             await asyncio.sleep(0.1)
#             balance -= amount
#             return  True
#         return False
#
# async def main():
#     task1,task2,task3 = await asyncio.gather(
#         withdraw(5000),
#         withdraw(500),
#         withdraw(100)
#     )
#     print(task1)
#     print(task2)
#     print(task3)
#
# asyncio.run(main())


# * asyncio.Event
# An Event lets one or more tasks wait until some condition occurs.

import asyncio
ready = asyncio.Event()

async def worker():
    print("Waiting...")
    await ready.wait()
    print("Starting Work")

async def initialize():
    await asyncio.sleep(2)
    ready.set()

async def main():
    await asyncio.gather(
        worker(),
        worker(),
        initialize()
    )

if __name__ == "__main__":
    asyncio.run(main())
