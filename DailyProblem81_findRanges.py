"""
Hi, here's your problem today. This problem was recently asked by Facebook:

Given a sorted list of numbers, return a list of strings that represent all of the consecutive numbers.

Example:
Input: [0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]
Output: ['0->2', '5->5', '7->11', '15->15']
Assume that all numbers will be greater than or equal to 0, and each element can repeat.

Here is a starting point:

def findRanges(nums):
  # Fill this in.

print findRanges([0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15])
# ['0->2', '5->5', '7->11', '15->15']
"""
def findRanges(nums):
    if len(nums) == 0:
        return []

    res = []
    k = nums[0]
    tmp = str(nums[0]) + '->'

    i = 0
    while i < len(nums):
        if k == nums[i]:
            k += 1
            i += 1
        elif k > nums[i]:
            i += 1
        else:
            tmp += str(k-1)
            res.append(tmp)
            tmp = str(nums[i]) + '->'
            k = nums[i]

    # deal with the last tmp string
    res.append(tmp + str(nums[-1]))
    return res

print(findRanges([]))

print(findRanges([0]))

print(findRanges([0, 1]))

print(findRanges([0, 1, 2]))

print(findRanges([0, 1, 2, 5, 7, 8, 9, 9, 10, 11]))
# ['0->2', '5->5', '7->11', '15->15']

print(findRanges([0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]))
# ['0->2', '5->5', '7->11', '15->15']