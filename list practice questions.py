list=[2,3,4,5,6,7,8,9]
list2=[ ]
i=0
while i<len(list):
    if list[i]%2==0:
        list.remove(list[i])
        list2.append(list[i])
        i+=1
print(list2)
        
    