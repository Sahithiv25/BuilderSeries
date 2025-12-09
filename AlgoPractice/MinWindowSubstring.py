# Minimum Window Substring

# given strings s and t, find the min window substring in s that contains al the characters from t. The substring must be contiguous. If there is no such substring, return the empty string "".
# Each character in t must appear in the window at least as many times as it appears in t.
# There is exactly one valid solution for each input.
# Characters in s can be reused as long as they are within the window; you do not "consume" them for t.
# Example:
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"

# Understand
# there are 2 strings s and t, we need to find the substring
# now, bruteforce is to check every possible substruing of s to see if it contains characters from t. It is inefficient for long strings.
# Optimal approach is using the sliding window with 2 pointers (left and right) 
# Now begin, take a hashmap and store the frequencies of characters of t in it.
# expand the window by moving the right pointer and cupdate the count.
# if the window contains all characters from t, then try to shrink the window by removing the characters from left to find the smallest possbile window.
# move the leeft pointer to remove unnecesaey char, updating the counts and ensuring the window still contains the required characters.
# each time a valid window is found, compare its length to the minimum found so far and update the lenth of the smallest.
# hashmap is used because the lookup only takes O(1).

from collections import Counter
class Solution:
    def minwindowsubstring(self, s:str, t:str) -> str:
        if not t or not s:
            return ""
        
        need = Counter(t) # freq map of char in t
        required = len(need) # how many unique char we need
        left, right = 0,0
        formed = 0 # how many unique char in the window met the required count
        window_counts = {}
        ans = float("inf"), None, None # best window seen so far (length, left_index, right_index)

        while right < len(s):
            character = s[right]
            window_counts[character] = window_counts.get(character,0) + 1

            if character in need and window_counts[character] == need[character]:
                formed+=1

            while left <= right and formed == required:
                character = s[l]
                if right - left + 1 < ans[0]:
                    ans = (right-left+1,left,right)
                window_counts[character] -= 1
                if character in need and window_counts[character] < need[character]:
                    formed -= 1
                l+=1
            r+=1
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2]+1]

# TC = O(n) each char is visited not more than twice (once by right and once by left)
# SC = O(m) for hashmaps
