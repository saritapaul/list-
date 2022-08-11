#Write a Python program to concatenate element-wise three given lists.
#Concatenate element-wise three said lists:
#['0red100', '1green200', '2black300', '3blue400', '4white500']
list=['0', '1', '2', '3', '4']
list1=['red', 'green', 'black', 'blue', 'white']
list2=['100', '200', '300', '400', '500']
i=0
new_list=[]
while i<len(list):
    a=list[i]+list1[i]+list2[i]
    new_list.append(a)
    i+=1
print(new_list)