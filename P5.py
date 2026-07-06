# 5. Longest Palindromic Substring
# Given a string s, return the longest palindromic substring in s.
# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
 

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_palin=""
        for i in range(len(s)):
           for j in range(i,len(s)):
              substring=s[i:j+1]

              if substring==substring[::-1]:
                 if len(substring)>len(max_palin):
                    max_palin=substring
        return max_palin


        
