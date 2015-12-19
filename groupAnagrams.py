# Group Anagrams
# https://leetcode.com/problems/anagrams/

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        h = {}
        for i in strs:
            s = ''.join(sorted(i))
            if s in h:
                h[s].append(i)
            else:
                h[s] = [i]
        res = []
        for i in h:
            res.append(sorted(h[i]))
        return res