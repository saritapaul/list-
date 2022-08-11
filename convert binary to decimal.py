binary_number=[1,1,0,1,1,0,0,1]
i=0
dec=0
while i<len(binary_number):
    if binary_number[i]==1:
        dec+=2**i
    i+=1
print(dec)