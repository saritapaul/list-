#Write a Python program to compute the average of n th elements in a given list oflists with different lengths.
list=[[0, 1, 2],[2, 3, 4], [3, 4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14]]
#Average of n-th elements in the said list of lists with different lengths:[4.8, 5.8, 6.8, 8.0, 11.0]
i=0
while i<len(list):
    j=0
    sum=0
    avg=0
    b=[ ]
    while j<len(list[i]):
     sum=sum+list[1][0]
     
     #b.append(avg)
     j+=1
    #avg=sum/len(list)
    i+=1
print(sum
