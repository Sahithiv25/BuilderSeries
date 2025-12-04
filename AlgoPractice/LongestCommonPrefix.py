
# Longest Common Prefix

# Understand: find the longest common prefix in an array of strings

# Vertical scanning = scanning column by column
# initialize min_length to identify the shortest string length
# Iterate through each string s in strs and update min_length to the min of min_length and length of s
# Initialize index i to - to get current char position
# while i is < min_length, iterate through each string s in strds
# if the char s[i] != char at strs[0][i] return the prefix strs[0][:i]
# increment i to check next character position
# return strs[0][:i] as longest common prefix after the loop

# Ex: ["flower", "flow", "flight"] answer is "fl"

from typing import List

class Solution:
    def LongestCommonPrefix(self, strs: List[str]) -> str:
        min_length = float('inf')
        for s in strs: # takes O(n)
            if len(s) < min_length:
                min_length = len(s)

        i = 0
        while i<min_length: # takes O(m)
            for s in strs:
                if s[i] != strs[0][i]:
                    return s[:i]
            i+=1

        return s[0][:i]    

# TC = O(n*m)

def longestCommonPrefix(strs):
    strs.sort() # takes O(n log n)
    first, last = strs[0], strs[-1]
    i = 0

    while i < len(first) and i < len(last) and first[i] == last[i]: # takes O(n)
        i += 1

    return first[:i]

# TC O(n log n)


