# Range Sum query 2D
# https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix(object):
    s = []
    r = -1
    c = -1
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        r = len(matrix)
        self.r = r-1
        if r==0:
            return
        c = len(matrix[0])
        self.c = c-1
        
        self.s = [ [0 for x in range(c)] for x in range(r)]
        
        for i in range(r):
            for j in range(c):
                self.s[i][j]+=matrix[i][j]
                if i>0:
                    self.s[i][j] += self.s[i-1][j]
                if j>0:
                    self.s[i][j] += self.s[i][j-1]
                if i>0 and j>0:
                    self.s[i][j] -= self.s[i-1][j-1]
                

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if row2>self.r or col2>self.c:
            return 0
        x = self.s[row2][col2]
        if row1 >0:
            x -= self.s[row1-1][col2]
        if col1>0:
            x -= self.s[row2][col1-1]
        if col1>0 and row1 >0:
            x += self.s[row1-1][col1-1]
        return x
        




# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.sumRegion(1, 2, 3, 4)