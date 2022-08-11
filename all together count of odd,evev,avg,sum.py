# count of odd and even numbers,sum of odd and even numbers,avg of odd and even numbers,total sum of elements,total avg of elements,total count of elements
elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
c=0
c_1=0
a=[]
a_1=[]
sum=0
sum1=0
avg=0
avg1=0
total_count=0
total_sum=0
total_avg=0
while i<len(elements):
    total_count=total_count+1
    total_sum=total_sum+elements[i]
    total_avg=total_sum/11
    if elements[i] % 2==0:
        a.append(elements[i])
        c+=1
        sum=sum+elements[i]
        avg=sum/4
    else:
        c_1+=1
        a_1.append(elements[i])
        sum1=sum1+elements[i]
        avg1=sum1/7
    i+=1
print("count of even numbers",c)
print("count of odd  numbers",c_1)
print("sum of even numbers",sum)
print("sum of odd numbers",sum1)
print("avg of even numbers",avg)
print("avg of odd numbers",avg1)
print("total sum of the elements",total_sum)
print("total number of elements",total_count)
print("total avg of elements",total_avg)