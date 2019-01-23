from math import sqrt

def squareRoot(a):
    return sqrt(a)


def firstStarDisplay():
    a=0
    while a<=7:
        print(a*"*")
        a+=1

def secondStarDisplay():
    for i in range(1,8) :
        print(i*'*')


def thirdStarDisplay():
    a=b=1
    while a<=7:
        while b<a:
            print("*",end="")
            b+=1
        a+=1
        b=a

def square(a,b):
    a=input('first number ')
    b=input('second number ')
    print("Square of {} * {} is {}".format(a,b,int(a)*int(b))) 