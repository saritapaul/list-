# Remove duplicates from list
list=[1,2,3,1,2,2]
list2=[]
i=0
while i<len(list):
    if list[i] not in list2:
        list2.append(list[i])
    i+=1
print(list2)