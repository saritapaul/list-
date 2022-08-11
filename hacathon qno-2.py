#Given an integer x, return true if x is palindrome integer.
#An integer is a palindrome when it reads the same backward as forward.
#For example, 121 is a palindrome while 123 is not.
#Example 1:Input: x = 121
#Input x= 10101
#Output: true
#Explanation: 121 reads as 121 from left to right and from right to left.
num=[1,2,1]
i=0
while i<len(num):
    m=num[i]
    i+=1
b=-1
c=0-len(num)
while b>=c:
    k=num[b]
    b-=1
if m==k:
    print("it is palindrome")
else:
    print("not palindrome")
    





