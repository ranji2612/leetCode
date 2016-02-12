# Longest Valid Parantheses
# https://leetcode.com/problems/longest-valid-parentheses/

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = []
        p = -1
        
        for i in s:
            p+=1
            if len(st)>0:
                if i==')':
                    x,k = st.pop()
                    if x=='(':
                        continue
                    else:
                        st.append((x,k))
                        st.append((i,p))
                else:
                    st.append((i,p))
            else:
                st.append((i,p))
        #Boundary
        st.insert(0,('',-1))
        st.append(('',p+1))
        m=0
        for i in range(1,len(st)):
            if st[i][1]-st[i-1][1] - 1>m:
                m = st[i][1]-st[i-1][1] - 1
            
        return m