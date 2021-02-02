import timeit
from memory_profiler import profile
from guppy import hpy
"QUESTION 1 TIME COMPLEXITY "
def f1():
    n=0
    for n in range(5000,10000):
        n=0
        if n==0:
            n+=1

        else:
            n+=2


def fonction():
    n = 0
    while n < 10000:
        n += 1


print(timeit.timeit(f1, number=50000))
print(timeit.timeit(fonction, number=50000))


"QUESTION 2 SPACE COMPLEXITY "
h=hpy(f1)
print(h.heap())

h=hpy(fonction)
print(h.heap())