# Last updated: 4/7/2025, 9:46:08 AM
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        re = []
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element != '.':
                    re += [(i, element), (element, j), (i // 3, j // 3, element)]
        return len(re) == len(set(re))