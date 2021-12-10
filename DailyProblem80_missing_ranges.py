"""
ref: https://www.geeksforgeeks.org/find-missing-elements-of-a-range/
Hi, here's your problem today. This problem was recently asked by Google:

Given a sorted list of numbers, and two integers low and high representing the lower and upper bound of a range, return a list of (inclusive) ranges where the numbers are missing. A range should be represented by a tuple in the format of (lower, upper).

Here's an example and some starting code:

def missing_ranges(nums, low, high):
  # Fill this in.
  
print(missing_ranges([1, 3, 5, 10], 1, 10))
# [(2, 2), (4, 4), (6, 9)]
"""
import bisect
def missing_ranges(nums, low, high):
    res = []
    nums.sort()
    # binary search for 'low' in sorted 
    # array and find index of first element 
    # which either equal to or greater than 
    # low. 
    i = bisect.bisect_left(nums, low)

    # Start from the found index and linearly 
    # search every range element n after this index
    n = low
    s, e = None, None

    while (i < len(nums) and n <= high):
        if nums[i] == n:
            if s and e:
                res.append((s, e))
            elif s:
                res.append((s, s))
            s, e = None, None
            i += 1
        elif nums[i] > n and s == None:
            s = n
        else:
            e = n
    # Move to next element in range [low, high] 
        n += 1
 
    # return the range of elements that are greater than the 
    # last element of sorted array. 
    if (n <= high): 
        res.append((n, high))
    return res
  
print(missing_ranges([1, 3, 5, 10], 1, 10))
# [(2, 2), (4, 4), (6, 9)]