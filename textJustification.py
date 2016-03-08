# Text Justification
# https://leetcode.com/problems/text-justification/

class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        L = []
        x = []
        wl= []
        if maxWidth==0:
            return [""]
        #Splitting the words first
        for i in words:
            if len(' '.join(x+[i]))<=maxWidth:
                x.append(i)
            else:
                L.append(x)
                wl.append(len(''.join(x)))
                x=[i]
        L.append(x)
        wl.append(len(''.join(x)))
        x=[i]
        #Assigning spaces - Even Covered
        for i in range(len(L)):
            nos = len(L[i]) - 1
            sp=1
            if i==(len(L)-1):
                L[i] = ' '.join(L[i])
                L[i] = L[i]+(' '*(maxWidth-len(L[i])))
            elif nos>0:
                while wl[i]+(sp+1)*nos<=maxWidth:
                    sp+=1
                y = maxWidth - (wl[i]+(sp)*nos)
                if y>0:
                    while y>0:
                        s1 = L[i].pop(0)
                        s2 = L[i].pop(0)
                        L[i]=[s1+(' '*(sp+1))+s2]+L[i]
                        y-=1
                L[i]=(' '*sp).join(L[i])
            else:
                L[i] = L[i][0]+' '*(maxWidth-len(L[i][0]))
        return L