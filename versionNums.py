# Version Numbers

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
            
        l1 = map(int,version1.split('.'))
        l2 = map(int,version2.split('.'))
        
        if len(l1)<len(l2):
            l1.extend([0]*(len(l2)-len(l1)))
        else:
            l2.extend([0]*(len(l1)-len(l2)))
        
        return cmp(l1,l2)