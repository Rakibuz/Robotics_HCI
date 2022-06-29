import _thread
import time

def print_epoch(nameOfThread,delay):
    count=0
    while count<3:
        time.sleep(delay)
        count+=1
        print(nameOfThread,"======",time.time())

_thread.start_new_thread(print_epoch,("thread 1",1)) #this thread will execute faster

_thread.start_new_thread(print_epoch,("thread 2",3)) #this thread will execute slow

input()