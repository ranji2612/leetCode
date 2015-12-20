# Valid Sudoku
# https://leetcode.com/problems/valid-sudoku/

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def check(n):
            #Hash speeded it up by 4ms :P
            s = {}
            for i in n:
                if i=='.':
                    continue
                if  i in s:
                    return False
                s[i] = 1
            return True
        def rowColCheck():
            rows = []
            cols = [[] for x in range(9)]
            for i in range(9):
                rows.append(board[i])
                for j in range(9):
                    cols[j].append(board[i][j])
            for i in range(9):
                if (not check(rows[i])) or (not check(cols[i])):
                    return False
            return True
        
        def boxCheck():
            i=0
            while i<9:
                j=0
                while j<9:
                    box = board[i][j:j+3]+board[i+1][j:j+3]+board[i+2][j:j+3]
                    if not check(box):
                        return False
                    j+=3
                i+=3
            return True
        #Dont do the box check if row check failed. So do row check first
        return rowColCheck() and boxCheck()