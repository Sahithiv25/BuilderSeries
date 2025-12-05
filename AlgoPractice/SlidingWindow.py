# Sliding Window - The concept
# Use 2 pointers that move across the array/string
# Use when there are : sub arras/sub strings, contigious elements, longest or shortest something, fixed size or variable size window
# Remove from left while expanding from right

# 2 types of sliding windows
# 1. Fixed window (window size=k)
# 2. Dynamic window (variable size) Ex: longest substring without repeating char, sumallest sub array

# LC 643 Maximum Sum of Subarray of size k
# Use sum of window, add right, remove left
# Ex: [1,2,3,4,5] k=3 output= [1,2,3]=6 [2,3,4]=9 [3,4,5]=12 this is how the window slides across array

# Think of the window with frame size k
# k covers exactly k contigious elements
# each slide moves right pointer to one step right and left pointer to one step right

# Initialize the first window with size k arr[:k]
# start sliding = the loop begins
# add new element entering the window window_sum += arr[right]
# remove the olf element leaving the window window_sum -= nums[left]
# inc the left ponter
# update max

# sliding window lets you maintain the running sum of fixrd size subarray. Instead of recomputing sums repeatedly,
# add the element in the window and remove ele leaving it. this makes the algorithm O(n) instead of O(n*k)

from typing import List

class Solution:
    def MaxSubarray(self, arr:List[int], k:int) -> int:
        window_sum = sum(arr[:k])
        max_sum = window_sum

        left = 0

        for right in range(k,len(arr)): # takes O(n)
            window_sum += arr[right]
            window_sum -= arr[left]
            left+=1
            max_sum = max(max_sum,window_sum)

        return max_sum
    

# LC 3: Longest substring without repeating characters
# find the longest substring




