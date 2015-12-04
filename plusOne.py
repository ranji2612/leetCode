# Plus One
# https://leetcode.com/problems/plus-one/

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        return map(int, list( str(1 + int(''.join( map(str, digits) ) ) ) ) )