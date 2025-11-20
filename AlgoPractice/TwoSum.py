# Problem: Find 2 numbers in an array that sum to a target value and return their indices

# Understand: 
# Get len of array
# Iterate through each index from 0 to n-1
# for each i, iterate through each index j from i+1 to n-1 using nested loop
# check if nums[i]+nums[j] equals target
# if true return containing the indices

from typing import List

# Brute Force
class Solution:
    def twoSum(self,nums:List[int],target:int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    return (i,j)

# TC: O(n^2)
# S: O(1)

# Optimal solution
# Use hashmap to achieve O(n) time complexity
# Initialize empty hash map to store numbers and their indices
# iterate through the arr with index i from 0 to length-1
# for each nums[i], compute the value as target-nums[i]
# check if y exists in hashmap and its index is not i
# if found return list containing i and index of y from hash map
# else add nums[i] and its index to hashmap

class Solution:
    def twoSum(self, nums:List[int],target:int) -> List[int]:
        hashmap = {} # dict
        for i in range(len(nums)): 
            hashmap[nums[i]] = i # hashmap is created ex: nums 1,2,3,4 hashmap is 1:0, 2:1, 3:2, 4:3
        
        for i in range(len(nums)):
            y = target-nums[i]
            if y in hashmap and hashmap[y] != i: # O(1) lookup
                return[i,hashmap[y]]
            
# TC = O(n)


            
