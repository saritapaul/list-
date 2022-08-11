# count unique values from list.
input_list=[1,2,2,5,8,4,4,8]
a=[]
c=0
i=0
while i<len(input_list):
    if input_list[i] not in a:
        a.append(input_list[i])
        c+=1
    i+=1
print(a,"count of unique values:-",c)  
    
       