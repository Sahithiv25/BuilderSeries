# Valid Anagram
# See whether two strings are anagrams 
# 1. they contain the same characters 
# 2. same frequencies

# Understand
# first check the length of the strings, if no then false
# use counter to determine the frequency of each character in string s 
# store this freq in s_dict
# use counter to count freq of each character in string t
# store this freq in t_dict
# compare s_dict & t_dict return true if they are equal

from collections import Counter

class Solution:
    def isAnagram(self, s:str, t:str) -> bool:
        if len(s) != len(t):
            return False
        count_s, count_t = {}, {}
        for i in s:  # takes O(n)
            if i in count_s:
                count_s[i] +=1 # takes O(1)
            else:
                count_s[i] = 1
        for j in t: # takes O(n)
            if j in count_t:
                count_t[j] += 1
            else:
                count_t[j] = 1
            
        return count_s==count_t
    
# TC = O(n)

# Using counter 

class Solution:
    def isAnagram(self, s: str, t:str) -> bool:
        if(len(s) != len(t)):
            return False
        return Counter(s) == Counter(t) # takes O(n) + O(n)

# TC = O(n)

# Optimized
# Sort and compare
class Solution:
    def isAnagram(self, s:str, t:str) -> bool:
        if(len(s) != len(t)):
            return False
        s = sorted(s) # sorting is O(n log n)
        t = sorted(t)
        if s == t: # comparing takes O(n)
            return True
        
# TC = O(n logn)