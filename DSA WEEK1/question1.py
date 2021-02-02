import timeit


def f1():
    for n in range(10000000):
        pass
f1()

def f2():
    n = 0
    while n < 100:
        n += 1

f2()
if __name__ == "__main__":
    print(timeit.timeit(f1, number=10000))
    print(timeit.timeit(f2, number=10000))
