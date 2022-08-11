#Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
#k is a positive integer and is less than or equal to the length of the linked list. 
# If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
#You may not alter the values in the list's nodes, only nodes themselves may be changed.
#Input: head = [1,2,3,4,5], k = 3
#Output: [3,2,1,4,5]
#Input l=[2,3,9,5,4,6,7],k=4
#Output: [4,5,9,3,2,6,7]
list=[1,2,3,4,5]
i=0
while i<len(list):
    a=list[2:0:-1]
    i+=1
print(a
    