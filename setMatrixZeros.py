# Set Matrix Zeros
# https://leetcode.com/problems/set-matrix-zeroes/

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = 0 if len(matrix[0])==0 else len(matrix[0])
        x = {}
        y = {}
        for i in range(m):
            for j in range(n):
                if not matrix[i][j]:
                    x[i] = 1
                    y[j] = 1
        for i in x:
            matrix[i] = [0 for k in range(n)]
        for j in y:
            for i in range(m):
                matrix[i][j] = 0