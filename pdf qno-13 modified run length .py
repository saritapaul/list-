# write a python program to create a list reflecting the modified run length encoding from 
# given list of intigers or a given list of character.output:[[2, 1], 2, 3, [2, 4], 5, 1]
list=[1,1,2,3,4,4,5,1]      
i=0
b=[]
while i<len(list): 
    k=list[i]
    d=0
    while i<len(list) and list[i]==k:  
        d=d+1
        i+=1
    if d>1:
        b.append([d,k])   
    else:
        b.append(k)
print(b)
        










       
