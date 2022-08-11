#Write a Python program to iterate a given list cyclically on specific index position.
#Iterate the said list cyclically on specific index position 3 :
#['d', 'e', 'f', 'g', 'h', 'a', 'b', 'c']
#Iterate the said list cyclically on specific index position 5 :
#['f', 'g', 'h', 'a', 'b', 'c', 'd', 'e']
a=int(input("enter no="))
list=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
#b=str(a-list)
while a<len(list):
    list2=[]
    list2.append(list[a])
    a+=1
print(list2)
j=0
while j<a:
    list2.append(list2[j])
    j+=1
print(list2

    
