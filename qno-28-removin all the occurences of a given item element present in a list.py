#The task is to perform the operation of removing all the occurrences of a given item/element present ina list.
#Explanation :The input list is [1, 1, 2, 3, 4, 5, 1, 2] and the item to be removed is 1.
#After removing the item, the output list is [2, 3, 4, 5, 2]
input=[1,1,2,3,4,5,1,2]
i=0
a=[]
while i<len(input):
    if input[i]!=1:
        a.append(input[i])
    i+=1
print(a)
        