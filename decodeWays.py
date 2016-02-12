# Decode Ways
# https://leetcode.com/problems/decode-ways/

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:
            return 0
        if s[0]=='0':
            return 0
        c = [0 for x in range(len(s))]
        c[0] = 1
        if len(s)>1:
            if s[1]=='0' and (int(s[0])>2 or int(s[0])<1):
                return 0
            else:
                c[1] = 1
            if s[1]!='0' and int(s[:2])<=26:
                c[1]+=1
            
        for i in range(2,len(s)):
            c[i] = c[i-1]
            if i>1 and int(s[i-1:i+1])<=26 and s[i-1]!='0':
                c[i]+= c[i-2]
            if s[i]=='0':
                if int(s[i-1])>2 or int(s[i-1])<1:
                    return 0
                else:
                    c[i] = c[i-2]
        return c[-1]