'''
Problem 283. Given an integer array nums, move all 0's to the end of it 
while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
'''

nums = [0,1,0,3,12]
# expected output: [1,3,12,0.0]

nums2 = [0,0,0,1,2,3,5]

# first approach:
for n in nums:
    if n == 0:
        temp = n
        nums.remove(n)
        nums.append(temp)
print(nums)

# second approach:
i = 0
j = 0
for i in range(len(nums2)):
    if nums2[i] != 0:
        nums2[j], nums2[i] = nums2[i], nums2[j]
        j += 1
print(nums2)