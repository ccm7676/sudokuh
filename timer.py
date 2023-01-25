import time
import _thread
total = 0

def timer():
    global total
    while True:
        time.sleep(1)
        total += 1

_thread.start_new_thread(timer, ("Thread-1", 2, ))
while True:
    print(total)
