#Write a Python program to find the dimension of a given matrix.
#Dimension of the said matrix:(2, 2)
#Dimension of the said matrix:(3,3)
list=[[1, 2], [2, 4]]
i=0
while i<len(list):
    j=0
    while j<len(list[i]):
        j+=1
    i+=1
print(i,j)