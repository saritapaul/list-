#You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Mergall the linked-lists into one sorted linked-list and return it.
#Example 1:
#Input: lists = [[1,4,5],[1,3,4],[2,6]]
#Output: [1,1,2,3,4,4,5,6]
#Explanation: The linked-lists are:
list=[[1,4,5],[1,3,4],[2,6]]
i=0
l=[ ]
while i<len(list):
    j=0
    while j<len(list[i]):
        a=list[i][j]
        c=0
        if a==1+c:
         l.append(a)
        j+=1
        c+=1
    i+=1
print(l)

