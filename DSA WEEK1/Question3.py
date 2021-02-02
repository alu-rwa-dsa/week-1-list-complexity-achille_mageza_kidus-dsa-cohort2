"Question3 -A"


def maximum(liste):
    maxi = liste[-1]
    for n in liste:
        if n > maxi:
            maxi = n
    return maxi


print(maximum([11, 1, 20, 101, 50, 3, 7, 100, 25]))

"QUESTION 3 -B"


#
def chaines():
    sentences = str(input("please enter the word or sentences in uppercase:"))
    sentences = sentences.upper()
    print(sentences.lower())

"EXMPLE 2"
pp="MASDJDSJNDJDNFEFNSJSCDNSDCOSDNCSDCNJNWDLCN"

def p():
    for i in pp :
        print(pp.lower())

p()

"QUESTION 3-D"
def liste():
    responde = int(input("enter the number that ypu want make the liste :"))
    a = [1, 100, 6, 40, 21, 45, responde]
    print(a)
    print("do you want to continuos")
    b = str(input("press no to stop or press ys to continuos"))
    if b=="yes":
    #
    #
        responde = int(input("enter the number that ypu want make the liste :"))
    #     # a = []
    #     # print(a)
    #     # print("do you want to continuos")
    #     # b = str(input("press no to stop or press yes to continuos"))
    #     responde = int(input("enter the number that you want make the liste :"))
    #     a1 = []
    #     a1.append(responde)
    #     c=a+a1
    #
    #     print(c)
    # else:
    #     if b=="no":
    #         print('thank you ')


liste()
