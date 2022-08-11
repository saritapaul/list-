list=[2,8,9,9,8,6,5,2]
list1=[ ]
list2=[]
i=0
while i<len(list):
    if list[i]not in list1:
        list1.append(list[i])
    else:
        list2.append(list[i])
    i+=1
print(list2)


