#Given the start and end of a range, write a Python program to print all negative numbers in a givenrange.
#Input: start = -4, end = 5
#Output: -4, -3, -2, -1
#Input: start = -3, end = 4
#Output: -3, -2, -1
a=int(input("enter no="))
b=int(input("enter number-"))
for i in range(a,b):
    if i<0:
       print(i,end=",")
