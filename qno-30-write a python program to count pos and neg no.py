#Given a list of numbers, write a Python program to count positive and negative numbers in a List.
list1 = [2, -7, 5, -64, -14]
#Output: pos = 2, neg = 3
#Iist2 = [-12, 14, 95, 3]
#Output: pos = 3, neg = 1
i=0
count=0
count1=0
while i<len(list1):
    if list1[i]>0:
        count+=1
    elif list1[i]<0:
        count1+=1
    i+=1
print(count)
print(count1)
        