#Python Threading Tutorial: Run Code Concurrently Using the Threading Module
#Source==https://www.youtube.com/watch?v=IEEhzQoKtQU

import concurrent.futures
import time
from unittest import result 

start=time.perf_counter()

def do_something(seconds):
    print(f'Sleeping  {seconds} second((s)...')
    time.sleep(seconds)
    return f'Done Sleeping..{seconds}'

with concurrent.futures.ThreadPoolExecutor() as executor:
   #-------------------map methods-----------(return the results in the order that they were started)
    secs=[5,4,3,2,1]
    results=executor.map(do_something,secs)

    for result in results:
        print(result)


    #---------------------as completed method---------(print out results in the order that they completed)
    # results=[executor.submit(do_something,sec) for sec in secs]
    # f1=executor.submit(do_something,1)
    # f2=executor.submit(do_something,1)
    # print(f1.result())
    # print(f2.result())
    for f in concurrent.futures.as_completed(results):
        print(f.result())


finish =time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
