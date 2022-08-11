#elements=[23,14,56,12,19,9,15,25,31,42,43]
list=[1,2,3,4,5,6]
list2=["one","two","three","four","five","six"]
list3=[]
i=0
while i<len(list):
    if list[i] not in list2:
        a=str(list[i])
        b=list2[i]
        c=a+b
        list3.append(c)
        list3.append(c)
    i+=1
print(list3)