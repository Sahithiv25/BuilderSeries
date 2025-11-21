# In a string s, return the index of first non-repeating character, if none return -1

# Understand
# You need to find out the character that is not duplicate
# create a hashmap and store the elements that have frequency more than 1
# if encountered an element with one freq first return that

class Solution:
    def firstUniqueChar(self, s:str) -> int:
        hashmap = {}
        for i in s: # takes O(n)
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1

        for i, c in enumerate(s): # takes O(n)
            if hashmap[c] == 1:
                return i
        return -1
    
# TC = O(n)

# Optimal
# by using counter

from collections import Counter

def firstUniqueCar(s:str) -> int:
    count = Counter(s)

    for i,c in enumerate(s):
        if count[c] == 1:
            return 1
    return -1
