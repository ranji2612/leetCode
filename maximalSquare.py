class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        #print matrix
        l = len(matrix)
        h = 0 if l==0 else len(matrix[0])
        D = [[0 for x in range(h)] for y in range(l)]
        if l>0:
            if matrix[0][0]=='1':
                D[0][0] = 1
        m = 0
        for i in range(l):
            for j in range(h):
                s = 1 if matrix[i][j]=='1' else 0
                if i>0 and j>0 and s>0:
                    s = min(D[i-1][j-1],D[i][j-1],D[i-1][j])+1
                D[i][j]=s
                if s>m:
                    m=s
            #print D
        return m*m