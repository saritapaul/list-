#Write a Python program to find the last occurrence of a specified item in a given list.
list=['s', 'd', 'f', 's', 'd', 'f', 's', 'f', 'k', 'o', 'p', 'i', 'w', 'e', 'k', 'c']
#Last occurrence of f in the said list:7
a=input("enter ch ")
i=0
while i<len(list):
    if list[i]==a:
      b=i
    i+=1
print(b)

