list=[50,40,23,70,56,12,5,10,7]
i=0
list1=list[i]
list2=list[i]
while i<len(list):
    if list[i]<list1:
        list1=list[i]
    if list[i]>list2:
        list2=list[i]
    i+=1
print(list1)
print(list2)
    
    