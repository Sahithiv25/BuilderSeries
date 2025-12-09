# Given two strings s1 and s2 return true if s1 contains a permutation of s2.

# Ex: s1 = "ab", s2 = "eidbaooo" output = true

# Understand
# check if string s2 contains a permutation of string s1 as a substring.
# Get lengths of both s1 and s2. if len(s1) > len(s2) then false
# initialize s1_counts and s2_counts as arrays of size 26 to store character freq for lowercase letters.
# for the first len(s1) characters, inc s1_counts for each char in s1 and s2_counts for each character in s2 using ord(char)-97 as index.
# check if s1_counts == s2_counts if true return true
# for each index i fron len(s1) to len(s2)-1
#   inc s2_counts for new char s2[i]
#   dec s2_counts for char s2[i-len(s1)] that left the window
#   id s1_counts equals s2_counts return true
# return false if permutation is not found.

# s1 = "ab", s2 = "eidbaooo" output = true

class Solution:
    def permutationinstring(seld, s1:str, s2:str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        if n1>n2:
            return False
        
        s1_counts = [0]*26
        s2_counts = [0]*26

        for i in range(n1): # takes O(n)
            s1_counts[ord(s1[i])-97] += 1
            s2_counts[ord(s2[i])-97] += 1

        if s1_counts == s2_counts:
            return True
        
        for i in range(n1,n2): # from n1 to n2-1  # takes O(n)
            # window size n1 is moving across n2
            # Ex: "ab" -> n1 = 2 window size = 2
            s2_counts[ord(s2[i]) - 97] += 1 # inc new char from s2 string
            s2_counts[ord(s2[i-n1]) - ord("a")] -= 1 # dec old char from s2 string
            if s1_counts == s2_counts:
                return True
            
        return False
    
# TC = O(n)
# SC = O(1)
