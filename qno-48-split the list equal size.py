#Write a Python program to split a given list into specified sized chunks.
list=[12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
#Split the said list into equal size 3[[12, 45, 23], [67, 78, 90], [45, 32, 100], [76, 38, 62], [73, 29, 83]]
i=0
a=[ ]
n=int(input("enter no "))
while i<len(list):
    c=(list[i:i+n])
    a.append(c)
    i+=n
print(a)