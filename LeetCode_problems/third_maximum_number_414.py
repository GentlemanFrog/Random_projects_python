'''
414. Third Maximum Number

Given an integer array nums, return the third distinct maximum number in this array. 
If the third maximum does not exist, return the maximum number.
'''

nums = [1,1,2]
# making list from set to get rid of duplicates
nums = list(set(nums))
# sorting reverse to have the max values in the beggining
nums.sort(reverse=True)

if len(nums) == 3 :
    print(min(nums))
elif len(nums) == 0 :
    print('-inf, empty list')
elif len(nums) < 3 :
    print(max(nums))

# in case which is not in previous 2 simple pops to get the third max value    
nums.pop(0)
nums.pop(0)

print(nums[0])