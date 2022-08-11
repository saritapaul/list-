# for example if we give 9119 the function shoud be return 811181,as the square of 9 is 81 and square of 1 is 1.
numbers=input("enter no: ")
i=0
sum=""
while i<len(numbers):
    num=int(numbers[i])**2
    sum=sum+str(num)
    i+=1
print(sum)