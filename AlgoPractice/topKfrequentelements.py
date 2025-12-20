# top k frequent elements
# given an array nums and integer k, return the k most frequent elements.

# Understand
# Ex: [1,1,1,2,2,3], k = 2
# output = [1,2]

# Basically finding Top-k

# take a new dict
# iterate through the numbers in list
# count freq of each element and store in dict
# sort the count in dict in reverse order
# return values based on k

from typing import List

class Solution:
    def topKfrequentelements(self, nums:List[int], k:int) -> List[int]:
        freq ={}
        for i in nums: # takes O(n)
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        sorted_items = sorted(freq.items(), key = lambda x:x[1], reverse = True) # takes O(mlogm)

        result = [item[0] for item in sorted_items[:k]]
        return result

# TC = O(nlog n)

# Optimal approach

# to get O(n) we must avoid sorting
# Trick: use buckets
# create a dict
# create buckets where bucket[i] will hold all numbers that appear i times
# walk backwards from right to left

class Solution:
    def topKFrequent(self, nums, k):
        freq = {}
        n = len(nums)
        for i in nums: # takes O(n)
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        bucket = [[] for _ in range(n+1)] # takes O(n)

        for num,count in freq.items():
            bucket[count].append(num)
        
        result = []
        bu = len(bucket)
        for i in range(bu-1,-1,-1): # takes O(n)
            if bucket[i]:
                result.extend(bucket[i])
            if len(result) == k: # stop when we got the k elements
                break
        return result
    
# TC = O(n)
# SC = O(n)