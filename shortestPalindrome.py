# Shortest Palindrime
# https://leetcode.com/problems/shortest-palindrome/

class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        if s==s[::-1]:
            return s
        i=0
        x = 0
        for i in range(l/2):
            if s[:(l/2 -i)][::-1]==s[(l/2)-i:(l/2)-i+(l/2)-i]:
                return s[l/2-i:][::-1]+s[l/2-i:]
            if s[:(l/2 -i)][::-1]==s[(l/2)-i+1:(l/2)-i+1+l/2 - i]:
                return s[l/2-i+1:][::-1]+s[l/2-i:]
        return s[1:][::-1]+s
        