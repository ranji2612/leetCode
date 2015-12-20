# Length of Last Word
# https://leetcode.com/problems/length-of-last-word/

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.split()
        s = '' if len(s)==0 else s[-1]
        return len(s)