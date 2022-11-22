'''
Given an integer array nums sorted in non-decreasing order, 
remove the duplicates in-place such that each unique element appears only once.
The relative order of the elements should be kept the same.
'''
nums = [0,0,1,1,1,2,2,3,3,4]

iterating = True
i=1
while iterating:
    if i < len(nums):
        # If previous in list is equal to current just pop it
        # we do it until i == to length of oour list if this happends
        # we break the loop
        if nums[i-1] == nums[i]:
            nums.pop(i-1)
        else:
            i+=1
    else:
        iterating = False
print(nums)