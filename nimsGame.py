# Nims Game
# https://leetcode.com/problems/nim-game/

class Solution(object):
    def canWinNim(self, n):
        return False if n%4 == 0 else True