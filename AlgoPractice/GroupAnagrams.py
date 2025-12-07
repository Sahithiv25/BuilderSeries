# Group Anagrams
# given an arr of strings group the anagrams together

# Understand
# Initialize a dict to group anagrams
# For each string in input list:
#   sort char in string
#   use sorted strin as key in the dictionary
#   append orginial string to the list corr to this key
# return the values of the dict as the result

from typing import List
from collections import defaultdict

class Solution:
    def GroupAnagrams(self, strs:List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs: # takes O(n)
            key = ''.join(sorted(s)) # takes O(mlog m)
            ans[key].appned(s)
        return list(ans.values())

# TC = O(n*(m log m))

#Optimal approach
# Use a frequency count of letters (array of size 26) as the key instead of sorting.
# For each string in the input list:
#   Count the frequency of each letter (O(K) time).
#   Use the tuple of counts as a key in the dictionary.
#   Append the original string to the list corresponding to this key.

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = defaultdict(list)
        for s in strs: # takes O(n)
            count = [0] * 26
            for c in s: # takes O(m)
                count[ord(c) - ord("a")] += 1
            key = tuple(count)
            anagrams_dict[key].append(s)
        return anagrams_dict.values()
    
# TC = O(n*m)
