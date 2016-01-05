# unique paths
# https://leetcode.com/problems/unique-paths/

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        #To support memoization
        self.c = [ [0 for x in range(n)] for x in range(m)]
        #There is only one way to open :P
        self.c[0][0] = 1
        def countPath(x,y):
            if self.c[x][y]>0:
                return self.c[x][y]
            else:
                val = 0
                if x!=0:
                    #Retract Up (if its not the top row)
                    val += countPath(x-1,y)
                if y!=0:
                    #Retract left (if its not the first col)
                    val +=  countPath(x,y-1)
                self.c[x][y] = val
                return val
        return countPath(m-1,n-1)