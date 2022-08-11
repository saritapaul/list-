#Write a Python program to join two given list of lists of same length, element wise.
list=[[10, 20], [30, 40], [50, 60], [30, 20, 80]]
list2=[[61], [12, 14, 15], [12, 13, 19, 20], [12]]
#Join the said two lists element wise:[[10, 20, 61], [30, 40, 12, 14, 15], [50, 60, 12, 13, 19, 20], [30, 20, 80, 12]]
i=0
new_list=[]
while i<len(list):
    a=list[i]+list2[i]
    new_list.append(a)
    i+=1
print(new_list)