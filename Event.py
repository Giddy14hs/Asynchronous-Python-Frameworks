# Importing the gevent library, which is used for asynchronous I/O and concurrency.
import gevent 

# Importing the monkey module from gevent. This allows gevent to modify the behavior of Python's standard library
# to make it cooperative (i.e., enable gevent's concurrency features).
from gevent import monkey

# Patching the standard library to use gevent's cooperative features (e.g., making network calls non-blocking).
monkey.patch_all()

# Importing the time module. Not used in this code but might be included for any timing/debugging purposes.
import time

# Defining the first task (task1). This function prints a start message, then sleeps for 1 second (without blocking).
# After the sleep, it prints that the task is done.
def task1():
    print("Task 1 starting")
    gevent.sleep(1)  # Simulates some work by sleeping for 1 second without blocking.
    print("Task 1 done")

# Defining the second task (task2). It sleeps for 2 seconds to simulate work and then prints a completion message.
def task2():
    print("Task 2 starting")
    gevent.sleep(2)  # Simulates work by sleeping for 2 seconds without blocking.
    print("Task 2 done")

# Defining the third task (task3). It sleeps for 3 seconds and prints that it's done.
def task3():
    print("Task 3 starting")
    gevent.sleep(3)  # Simulates work by sleeping for 3 seconds without blocking.
    print("Task 3 done")

# This section spawns three greenlets (lightweight concurrent "threads" managed by gevent) for task1, task2, and task3.
# Each task is run concurrently (non-blocking) using gevent.spawn.
# gevent.joinall ensures that the main program waits until all the tasks (greenlets) are completed.
gevent.joinall([
    gevent.spawn(task1),  # Spawning task1 as a greenlet.
    gevent.spawn(task2),  # Spawning task2 as a greenlet.
    gevent.spawn(task3),  # Spawning task3 as a greenlet.
])
