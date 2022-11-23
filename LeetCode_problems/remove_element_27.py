'''
Problem 27. Given an integer array nums and an integer val, remove all occurrences of val in nums 
in-place. The relative order of the elements may be changed.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array
in-place with O(1) extra memory.
'''
nums = [3,2,2,3]
val = 3

if len(nums) == 0:
    print(0)
j = 0
for i in range(len(nums)):
    if nums[i] != val:
        nums[j] = nums[i]
        j += 1
print(j)