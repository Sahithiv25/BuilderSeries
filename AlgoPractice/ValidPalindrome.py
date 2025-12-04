# Valid Palindrome

# Get length n = len(s) of string s
# initialize 2 pointers: L to 0 (start) and R to n-1 (end)
# while L < R
#   if char at s[L] is not alphanumeric, inc L and continue
#   if char at s[R] is not alphanumeric, dec R and continue
#   if lowercase char at s[L] and s[R] are not equal return False
# Inc L and rec R to check the next pair
# return true if matched

class Solution:
    def ValidPalindrome(self, s:str) -> str:
        n = len(s)
        l = 0
        r = n-1
        while l<r: # takes O(n)
            if not s[l].isalnum():
                l+=1
                continue
            if not s[r].isalnum():
                r-=1
                continue
            if s[l].lower() != s[r].lower():
                return False
            
            l+=1
            r-=1
        return True
    
# TC = O(n)

# this approach avoids creating new string. 
# take 2 pointers and compare them to the mid and not uses any additional loops