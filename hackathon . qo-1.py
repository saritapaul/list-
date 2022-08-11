#Given an array of integer numbers and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.
#Example 1:Input: nums = [2,7,11,15], target = 9 , target = 18
#Output: [0,1]Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
num=[2,7,11,15]
i=0
sum=0
l=[ ]
while i<len(num):
    sum=sum+num[i]
i+=1
print(sum
