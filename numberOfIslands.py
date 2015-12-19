# Number of Islands
# https://leetcode.com/problems/number-of-islands/

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        d = len(grid)
        l = 0 if d==0 else len(grid[0])
        
        def dfs_spread(a,b):
            grid[a][b] = -1
            if b-1>=0 and grid[a][b-1]=="1":
                dfs_spread(a,b-1)
            if a-1>=0 and grid[a-1][b]=="1":
                dfs_spread(a-1,b)
            if a+1<d and grid[a+1][b]=="1":
                dfs_spread(a+1,b)
            if b+1<l and grid[a][b+1]=="1":
                dfs_spread(a,b+1)
        count = 0
        for i in xrange(d):
            for j in xrange(l):
                if grid[i][j]=="1":
                    count += 1
                    dfs_spread(i,j)
        return count