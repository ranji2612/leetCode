# Surrounded Regions
# https://leetcode.com/problems/surrounded-regions/

# DFS will fail because of recursion depth problem.
# So use BFS.

# Custom Test case  : [["X", "X", "X", "X"],["X", "O", "O", "O"],["X", "O", "O", "X"],["X", "O", "X", "X"]]


class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        d = len(board)
        l = 0 if d==0 else len(board[0])
        
        def bfsVisit(a,b):
            Q = [(a,b)]
            while len(Q)>0:
                (a,b) = Q.pop(0)
                board[a][b]="1"
                if a-1>=0 and board[a-1][b]=="O":
                    Q.append((a-1,b))
                    board[a-1][b]="1"
                
                if b-1>=0 and board[a][b-1]=="O":
                    Q.append((a,b-1))
                    board[a][b-1]="1"
                
                if a+1<d and board[a+1][b]=="O":
                    Q.append((a+1,b))
                    board[a+1][b]="1"
                
                if b+1<l and board[a][b+1]=="O":
                    Q.append((a,b+1))
                    board[a][b+1]="1"
            
        for i in range(d):
            if i==0 or i==d-1:
                for j in range(l):
                    if board[i][j]=="O":
                        bfsVisit(i,j)
            else:
                if len(board[i])>0 and board[i][0]=="O":
                    bfsVisit(i,0)
                if len(board[i])>0 and board[i][l-1]=="O":
                    bfsVisit(i,l-1)
        for i in range(d):
            for j in range(l):
                if board[i][j]=="O":
                    board[i][j] = "X"
                if board[i][j]=="1":
                    board[i][j] = "O"