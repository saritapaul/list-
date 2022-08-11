elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
c=0
c_1=0
a=[]
a_1=[]
while i<len(elements):
        if elements[i]%2==0:
            c=c+1
            a.append(c)
        else:
            c_1=c_1+1
            a_1.append(c_1)
        i=i+1
print("even number=",c)
print("odd number=",c_1)