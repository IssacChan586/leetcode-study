"""
编写一个程序，通过已填充的空格来解决数独问题。
一个数独的解法需遵循如下规则：
数字1-9在每一行只能出现一次。
数字1-9在每一列只能出现一次。
数字1-9在每一个以粗实线分隔的3x3宫内只能出现一次。
空白格用'.'表示。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sudoku-solver
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def get_block(col: int, row: int) -> int:
            return row // 3 * 3 + col // 3

        def backtracking(board: List[List[str]], col: int, row: int, row_lack: List[List[str]],
                         col_lack: List[List[str]],
                         block_lack: List[List[str]]) -> bool:
            if col == 0 and row == len_board:
                return True
            (next_col, next_row) = (col + 1, row) if col < len_board - 1 else (0, row + 1)
            if board[row][col] != '.':
                return backtracking(board, next_col, next_row, row_lack, col_lack, block_lack)
            for i in range(1, len_board + 1):
                ch = str(i)
                if ch in row_lack[row] and ch in col_lack[col] and ch in block_lack[get_block(col, row)]:
                    row_lack[row].remove(ch)
                    col_lack[col].remove(ch)
                    block_lack[get_block(col, row)].remove(ch)
                    board[row][col] = ch
                    if backtracking(board, next_col, next_row, row_lack, col_lack, block_lack):
                        return True
                    board[row][col] = '.'
                    row_lack[row].append(ch)
                    col_lack[col].append(ch)
                    block_lack[get_block(col, row)].append(ch)
            return False

        len_board = len(board)
        row_lack = [[str(i) for i in range(1, 10)] for _ in range(10)]
        col_lack = [[str(i) for i in range(1, 10)] for _ in range(10)]
        block_lack = [[str(i) for i in range(1, 10)] for _ in range(10)]
        for row in range(len_board):
            for col in range(len_board):
                if board[row][col] != '.':
                    row_lack[row].remove(board[row][col])
                    col_lack[col].remove(board[row][col])
                    block_lack[get_block(col, row)].remove(board[row][col])
        if backtracking(board, 0, 0, row_lack, col_lack, block_lack):
            return


if __name__ == '__main__':
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    Solution().solveSudoku(board)
    for i in range(9):
        print(board[i])
