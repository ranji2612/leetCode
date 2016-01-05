# unique paths 2
# https://leetcode.com/problems/unique-paths-ii/

class Solution(object):
    c = []
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        #If the final step is an obstacle or the opening step
        if obstacleGrid[m-1][n-1]==1 or obstacleGrid[0][0]==1:
                return 0
        #Array for memoization
        self.c = [ [-1 for x in range(n)] for x in range(m)]
        #Setting the value for the opening step - only one way to start
        self.c[0][0] = 1
        #Recursion with memoization
        def countPath(x,y):
            if self.c[x][y]>-1:
                #If already calculated , return the value
                return self.c[x][y]
            else:
                val = 0
                if x!=0:
                    #Set the value only if there is no obstacle
                    val += countPath(x-1,y) if obstacleGrid[x-1][y]==0 else 0
                if y!=0:
                    #Set the value only if there is no obstacle
                    val += countPath(x,y-1) if obstacleGrid[x][y-1]==0 else 0
                #Add to the array that the val is computed for x,y & return
                self.c[x][y] = val
                return val
        return countPath(m-1,n-1)