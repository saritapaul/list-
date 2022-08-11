# our task is to print the elements which occurs consecutive times in a python list.
#list=[4,5,5,5,3,8]
list=[1,1,1,64,23,64,22,22,22]
i=0
a=[ ]
while i<len(list)-1:
   if list[i]==list[i+1] and list[i+1]==list[i+2]:
     a.append(list[i])
   i+=1
print(a)

