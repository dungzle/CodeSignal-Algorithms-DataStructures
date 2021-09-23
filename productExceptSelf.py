"""
- You have an array nums. We determine two functions to perform on nums. In both cases, n is the length of nums:

	fi(nums) = nums[0] · nums[1] · ... · nums[i - 1] · nums[i + 1] · ... · nums[n - 1]. ( fi(nums) = product of all array elements except the ith)
	g(nums) = f0(nums) + f1(nums) + ... + fn-1(nums).
	Using these two functions, calculate all values of f modulo the given m. Take these new values and add them together to get g. You should return the value of g modulo the given m.

- Example

	For nums = [1, 2, 3, 4] and m = 12, the output should be
	productExceptSelf(nums, m) = 2.

	The array of the values of f is: [24, 12, 8, 6]. If we take all the elements modulo m, we get:
	[0, 0, 8, 6]. The sum of those values is 8 + 6 = 14, making the answer 14 % 12 = 2.

- Input/Output

	[execution time limit] 4 seconds (py3)

	[input] array.integer nums

	Guaranteed constraints:
	2 ≤ nums.length ≤ 2 · 105,
	1 ≤ nums[i] ≤ 100.

	[input] integer m

	Guaranteed constraints:
	2 ≤ m ≤ 105.

	[output] integer
"""

import numpy as np
def productExceptSelf(nums, m):
    left_prod = np.empty(len(nums),dtype='int')
    right_prod = np.empty(len(nums),dtype='int')
    left_prod[0] = 1
    right_prod[len(nums)-1] = 1
    for i in range(1,len(nums)):
        left_prod[i] = (left_prod[i-1] * nums[i-1]) % m
    for i in range(len(nums)-2,-1,-1):
        right_prod[i] = (right_prod[i+1] * nums[i+1]) % m
    return (np.sum(left_prod*right_prod) % m)
        