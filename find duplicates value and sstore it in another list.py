n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
i=0
m=[]
o=[]
j=[]
while i<len(n):
    if n[i] not in m:
        m.append(n[i])
    else:
        o.append(n[i])
    i+=1
print(o) 