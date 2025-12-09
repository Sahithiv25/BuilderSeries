# LC Container with most water
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.

# Ex: height = [1,8,6,2,5,4,8,3,7] Output: 49
# Explanation The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

# Understand 
# find 2 lines that can form a container with max water area given an array of heights
# can do this using 2 pointer solution
# initialize left pointer to 0 and right pointer to the len(arr)-1.
# initialize max_area=0 to track the max area that is found
# while l<r calculate the width as r-l
# calculate the height as minimum of height[left],height[right]
# area = widthXheight and update max_area if the computed area is large
# if height[l] < height[r] inc l othervise dec r
# return max area after the loop

from typing import List
class Solution:
    def containerwithmostwater(self, height:List[int]) -> int:
        n = len(height)
        l,r = 0,n-1
        max_area = 0

        while l<r: # takes O(n)
            w = r - l
            h = min(height[l],height[r])
            area_of_container = w * h
            max_area = max(max_area,area_of_container)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area

# TC = O(n)
# SC = O(1)