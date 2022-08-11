#Write a code that checks whether a list is a palindrome or not. 
#And print “Haan! palindrome hai” if its a pallindrome and “nahi! palindrome nahi hai” if its not a palindrome.
name=["n","i","t","i","n"]
#i=0
#a=-1
#while i<len(name):
#    c=name[i]
#    i+=1
 #   d=name[a]
#    a-=1
#if c==d:
#    print(c)
#else:
#    print("nahi!palindrome nahi hai") 
i=0
while i<len(name):
    m=name[i]
    i+=1
b=-1
c=0-len(name)
while b>=c:
    k=name[b]
    b-=1
if m==k:
    print(k)
else:
    print("not palindrome")








