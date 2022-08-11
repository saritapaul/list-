#Given a List, extract all elements whose frequency is greater than K.
test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
#K = 3
#Output: [4, 3]
#Explanation: Both elements occur 4 times.
#test_list2 = [4, 6, 4, 3, 3, 4, 3, 4, 6, 6]
#Output: [4, 3, 6]
#Explanation: Occur 4, 3, and 3 times respectively.
i=0
list=[]
list2=[]
count=0
while i<len(test_list):
    if test_list[i] not in list:
        list.append(test_list[i])
    else:
        list2.append(test_list[i])
    i+=1
print(list2
    