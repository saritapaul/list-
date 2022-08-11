# #Write a Python program to pair up the consecutive elements of a given list.
# #Pair up the consecutive elements of the said list:[[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
# #lists=[1, 2, 3, 4, 5]
# #Pair up the consecutive elements of the said list:[[1, 2], [2, 3], [3, 4], [4, 5]]
# #list=[1, 2, 3, 4,5,6]
# #i=0
# #a=[]
# #while i<len(list):
# #    c=(list[i:i+2])
# #    a.append(c)
# #    i+=1
# #print(a
list=[1,2,3,4,5]
i=1
a=[ ]
while i<len(list):
    a.append([list[i]-1]+[list[i]])
    i=i+1
print(a)