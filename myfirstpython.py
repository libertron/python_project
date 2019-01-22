#coding:utf-8
#print("Hello world")
# a="Hello world"
# def myfunction(name):
#     print("hello"+name)
# myfunction("Stanj")
def square(a,b):
    return a*b
a=input('first number ')
b=input('second number ')
# print("square of "+str(a)+" and "+str(b)+" is "+str(square(int(a),int(b))))
print("square of {0} and {1} is {2} ".format(a,b,square(int(a),int(b))))