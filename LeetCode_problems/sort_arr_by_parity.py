'''
Problem 905. Given an integer array nums, move all the even integers at the beginning of the
array followed by all the odd integers.

Return any array that satisfies this condition.
'''
nums = [3,1,2,4]

l = 0
r = len(nums)-1
while l < r:
    if nums[l]%2 == 1:
        if nums[r]%2 == 0:
            nums[l], nums[r] = nums[r], nums[l]
        else: r -= 1
    else: l += 1
print(nums)