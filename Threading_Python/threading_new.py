#Python Threading Tutorial: Run Code Concurrently Using the Threading Module
#Source==https://www.youtube.com/watch?v=IEEhzQoKtQU
import threading
import time 

start=time.perf_counter()

def do_something(seconds):
    print(f'Sleeping  {seconds}second...')
    time.sleep(seconds)
    print('Done Sleeping..')
     
threads=[]

for _ in range(10):
    t=threading.Thread(target=do_something,args=[1.5])
    t.start()
    threads.append(t)
    

for thread in threads:
    thread.join()



# t1=threading.Thread(target=do_something)
# t2=threading.Thread(target=do_something)

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# do_something()
# do_something()


finish =time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
