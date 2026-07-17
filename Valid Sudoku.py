class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[False] * 9 for _ in range(9)]
        cols = [[False] * 9 for _ in range(9)]
        boxes = [[False] * 9 for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j]) - 1
                    boxindex = (i // 3) * 3 + (j // 3)#peranthasis for preference

                    if rows[i][num] or cols[j][num] or boxes[boxindex][num]:
                        return False

                    rows[i][num] = cols[j][num] = boxes[boxindex][num] = True

        return True