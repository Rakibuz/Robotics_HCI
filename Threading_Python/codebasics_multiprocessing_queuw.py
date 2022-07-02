#source=https://github.com/codebasics/py/blob/master/Multiprocessing/multiprocessing_queue_pipe.py
import multiprocessing

def calc_square(numbers, q):
    for n in numbers:
        q.put(n*n)

if __name__ == "__main__":
    numbers = [2,3,5]
    q = multiprocessing.Queue() #queue is basically shared memory
    p = multiprocessing.Process(target=calc_square, args=(numbers,q))

    p.start()
    p.join()

    while q.empty() is False:
        print(q.get())

#   multiprocessing queue --------------------vs --------------------queue module
#  Lives in shared memory  ----------        ---   -----  lives in in process memory
#  used to share data between process----- -----------used to share data between threads