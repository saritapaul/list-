#Write a Python program to remove all the values except integer values from a givenarray of mixed values.
list=[34.67, 12, -94.89, 'Python', 0, 'C#']
#After removing all the values except integer values from the said array of mixed values:[12,0]
i=0
a=[]
while i<len(list):
    j=list[i]
    if type(j)==int:
        a.append(j)
    i+=1
print(a)