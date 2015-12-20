# Substring with Concatenation of all words
# https://leetcode.com/problems/substring-with-concatenation-of-all-words/

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        def buildHash():
            h = {}
            for i in words:
                if i in h:
                    h[i] += 1
                else:
                    h[i] = 1
            return h
        #Check hash
        def checkHash():
            for i in h:
                if h[i]!=0:
                    return False
            return True
        
        def valid(ps,l):
            i=0
            while i< len(ps):
                if ps[i:i+l] in h:
                    h[ ps[i:i+l] ] -= 1
                i+=l
            return True
        
        if len(words)==0:
            return []
        #Hash the words
        h = {}
        buildHash()
        #length of each word
        l = len(words[0])
        tl = l*len(words)
        
        i=j=0
        ls = len(s)
        res = []
        while j<l:
            h = buildHash()
            i = j
            ps = s[i:i+tl]
            valid(ps,l)
                
            while i<ls-tl+1:
                #print '-'*10,i,h
                #Remove i : i + l
                if i>=l and s[i-l:i] in h:
                    #print 'adding ',s[i-l:i],h
                    h[ s[i-l:i] ] += 1
                #Add i+tl:i+tl+l
                if i>=l and s[i+tl-l:i+tl] in h:
                    #print 'removing ',s[i+tl-l:i+tl]
                    h[ s[i+tl-l:i+tl] ] -= 1
                #Check if ps is valid
                if checkHash():
                    res.append(i)
                i+=l
            j+=1
        return res