import matplotlib.pyplot as plt

# def maximum2():
responde = int(input("enter the number that ypu want make the liste :"))
a = [1, 100, 6, 40, 21, 45, responde]
print(a)


plt.xticks( range(1,10000), a)
y=[1,2,3,4,5,6,7]
x=[1,2,3,4,5,6,7]
plt.plot(y)
plt.plot(x)
# plt.plot(lst, time_t)
plt.xlabel("List of element")
plt.ylabel("Time complexity")
plt.show()


