#source=https://www.youtube.com/watch?v=Lu5LrKh1Zno&list=PLeo1K3hjS3uub3PRhdoCTY8BxMKSW7RjN&index=2
import time
import multiprocessing

square_result=[]

def calc_square(numbers):
    global square_result
    for n in numbers:
        #time.sleep(5)
        print('square ' + str(n*n))
        square_result.append(n*n)
    print('within a process reuslt'+ str(square_result))

def calc_cube(numbers):
    for n in numbers:
        time.sleep(5)
        print('cube ' + str(n*n*n))

if __name__ == "__main__":
    arr = [2,3,8]
    p1 = multiprocessing.Process(target=calc_square, args=(arr,))
    #p2 = multiprocessing.Process(target=calc_cube, args=(arr,))

    p1.start()
   # p2.start()

    p1.join()
    #p2.join()
    
    print('reuslt'+ str(square_result))
    print("Done!")


    # --------------here output---
        # square 4
        # square 9
        # square 64
        # within a process reuslt[4, 9, 64]
        # reuslt[]
        # Done!

    # if we have used multithreading  reuslt[] would be like reuslt[4, 9, 64]
    #this is the basic difference between multithreading and multiprocessing. as multi threading share same address space