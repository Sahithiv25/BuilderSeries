# 3 Sum

# given an integer array nums, return all the triplets [nums[i],nums[j],nums[k]] such that i != j, i != k and j != k and nums[i],nums[j],nums[k] == 0
# solution set must not contain duplicate triplets.

# Ex: nums = [-1,0,1,2,-1,-4] output = [[-1,-1,2],[-1,0,1]]

# Understand:
# create a hashmap h[num] = i
# use set to remove duplicates
# iterate over all pairs of elements use 2 nested loops i,j to select every unique pair of elements from nums
# for each pair (nums[i],nums[j]) find 3rs number = -nus[] - nums[j]
# try to find 3rd number that makes sum = 0
# check if desired exists in hashmap and is not same as i or j
# if found add the triplet to the set after sorting it to avoid permutations.
# return set containing all unique triplets that sum to 0

from typing import List
class Solution:
    def ThreeSum(self, nums: List[int]) -> List[List[int]]:
        h = {} # hashmap
        n = len(nums)
        s = set()

        for i, num in enumerate(nums):
            h[num] = i
        
        for i in range(n):
            for j in range(i+1,n):
                desired = -nums[i] - nums[j]
                if desired in h and h[desired] != i and h[desired] != j:
                    s.add(tuple(sorted([nums[i],nums[j],desired])))
        return s
    
# TC = O(n^2)
# SC = O(n)

# Another optimal solution is to use 2 pointers O(n^2)