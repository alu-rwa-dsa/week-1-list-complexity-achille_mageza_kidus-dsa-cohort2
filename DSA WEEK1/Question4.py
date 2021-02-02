import matplotlib.pyplot as plt
import time


def maximum(liste):
    maxi = liste[-1]
    time_t = []
    second_1 = time.time()
    for n in liste:
        if n > maxi:
            maxi = n
        second_2 = time.time()
        total_time = second_2 - second_1
        time_t.append(total_time)
    return maxi, time_t


lst = list(range(0, 1000000))
maxi, time_t = maximum(lst)

plt.plot(lst, time_t)
plt.xlabel("List of element")
plt.ylabel("Time complexity")
plt.show()

# plt.plot(lst, space)
# plt.xlabel("List of element")
# plt.ylabel("Space complexity")
# plt.show()
