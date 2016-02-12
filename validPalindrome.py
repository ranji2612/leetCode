class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = re.sub('[^a-zA-Z0-9]','',s.lower())
        return True if s == s[::-1] else False