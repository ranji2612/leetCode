# Add Binary
# https://leetcode.com/problems/add-binary/

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        c=0
        s = ''
        while a!='' or b!='':
            n = 0
            if a!='':
                n+=int(a[-1])
                a=a[:-1]
            if b!='':
                n+=int(b[-1])
                b=b[:-1]
            s+=str((n+c)%2)
            c = 1 if (n+c)>1 else 0
        if c>0:
            s+='1'
        return s[::-1]