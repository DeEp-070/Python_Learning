# * creating a process
# from multiprocessing import Process
#
# def task(number:int )->None:
#     print(f"Process is running and the number is :- {number}")
#
#
# if __name__ == "__main__":
#     process = Process(target=task,args=(10,))
#     process.start()
#     process.join()

# * Creating multiple process
# from multiprocessing import Process
# import math
#
# def calculate(num:int)->None:
#     print(math.pow(num,2))
#
# processes = []
# if __name__ == "__main__":
#     for number in [10,20,30,40]:
#         process = Process(
#             target=calculate,
#             args=(number,)
#         )
#
#         processes.append(process)
#         process.start()
#     for process in processes:
#         process.join()

# *Inter-Process Communication
# *Python provides mechanisms such as:-
# *Queue
# *Pipe
# *shared memory
# *managers
#
# #Queue
# from multiprocessing import Process, Queue
#
#
# def worker(queue):
#     queue.put("Task completed")
#
# queue = Queue()
#
# if __name__ == "__main__":
#     process = Process(
#         target=worker,
#         args = (queue,)
#     )
#     process.start()
#     result = queue.get()
#     process.join()
#     print(result)


# *Process pools
#
# from concurrent.futures import ProcessPoolExecutor
#
# def square(number:int)->int:
#     return number*number
#
# if __name__ == "__main__":
#     with ProcessPoolExecutor(max_workers=4) as executor:
#         results = executor.map(
#             square,
#             [1,3,4,5]
#         )
#
#         print(list(results))


# **GIL
# GIL = Global Interpreter Lock.
#
# In standard CPython, the GIL is a mechanism that limits multiple threads from executing Python bytecode
# simultaneously within the same interpreter in the traditional CPython execution model.

# *Important Modern CPython Note
#
# *Modern CPython development has introduced free-threaded builds that can run without the traditional GIL
# *under supported configurations.
#
# For your learning roadmap, however, you should understand the traditional GIL model because:
#
# *much existing Python software uses it
# many production deployments use standard GIL-enabled CPython
# it remains important for understanding Python concurrency
# *library compatibility and runtime configuration matter
#
# *So don't build your mental model around "GIL no longer matters."

# *Serialization / Pickling
#
# When data needs to move between processes, Python may need to serialize it.
#
# A common mechanism is pickle.
#
# *For example, process-based executors often need to serialize:
#
# function/task
# arguments
# results
#
# *This means not every Python object is equally convenient to send between processes.
#
# For example, local nested functions and certain objects can cause problems.
#
# *This becomes particularly relevant when designing multiprocessing systems.