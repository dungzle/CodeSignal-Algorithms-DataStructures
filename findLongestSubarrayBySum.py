"""
    You have an unsorted array arr of non-negative integers and a number s. 
    Find a longest contiguous subarray in arr that has a sum equal to s. 
    Return two integers that represent its inclusive bounds. 
    If there are several possible answers, return the one with the smallest left bound. If there are no answers, return [-1].

Your answer should be 1-based, meaning that the first position of the array is 1 instead of 0.

Example

For s = 12 and arr = [1, 2, 3, 7, 5], the output should be
findLongestSubarrayBySum(s, arr) = [2, 4].

- Input/Output

[execution time limit] 4 seconds (py3)

[input] integer s

The sum of the subarray that you are searching for.

Guaranteed constraints:
0 ≤ s ≤ 109.

[input] array.integer arr

The given array.

Guaranteed constraints:
1 ≤ arr.length ≤ 105,
0 ≤ arr[i] ≤ 104.

[output] array.integer

An array that contains two elements that represent the left and right bounds of the subarray, respectively (1-based). If there is no such subarray, return [-1].
"""
def findLongestSubarrayBySum(s, arr):
    i,j = (0,0)
    max_length = -1
    start,end = (0,0)
    temp_sum = 0 
    while j < len(arr):
        temp_sum += arr[j]
        while temp_sum > s:
            temp_sum -= arr[i]
            i += 1
        if temp_sum == s:
            if max_length < (j-i):
                max_length = (j-i)
                start,end = (i+1,j+1) 
        j += 1
    if max_length < 0:
        return [-1]
    return (start,end)