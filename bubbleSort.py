from random import randint
from time import ctime, clock
def timeUsed(func):
    def timeUse(*arg):
        timeTemp = clock()
        ret = func(*arg)
        timeTemp2 = clock()
        print('%sActual used time:%0.3fs'%(func.__name__, timeTemp2-timeTemp))
        return ret
    return timeUse

@timeUsed
def bubbleSort(alist):
    for i in range(len(alist)-1,0,-1):
        for j in range(i):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]

alist = [randint(0,10000) for i in range(10000)]
bubbleSort(alist)
# print(alist)
