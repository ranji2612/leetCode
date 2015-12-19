# Valid Anagrams
# https://leetcode.com/problems/valid-anagram/

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        h = {}
        for i in s:
            if i in h:
                h[i] += 1
            else:
                h[i] = 1
        for i in t:
            if not i in h:
                return False
            else:
                h[i] -= 1
                if h[i] == 0:
                    del h[i]
        if len(h)==0:
            return True
        return False