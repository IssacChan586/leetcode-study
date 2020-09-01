"""
https://leetcode-cn.com/problems/surrounded-regions/
130. 被围绕的区域
给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。
找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。

示例:
X X X X
X O O X
X X O X
X O X X

运行你的函数后，矩阵变为：
X X X X
X X X X
X X X X
X O X X
解释:
被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
"""
from typing import List


class Solution:

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 0 or len(board[0]) == 0:
            return

        def dfs(new_board: List[List[str]], y: int, x: int):
            if y < 0 or x < 0 or y >= len(new_board) or x >= len(new_board[0]) \
                    or new_board[y][x] == '#' or new_board[y][x] == 'X':
                return
            new_board[y][x] = '#'
            dfs(new_board, y - 1, x)
            dfs(new_board, y + 1, x)
            dfs(new_board, y, x - 1)
            dfs(new_board, y, x + 1)

        height = len(board)
        width = len(board[0])
        for y in range(height):
            for x in range(width):
                is_edge = y == 0 or x == 0 or y == height - 1 or x == width - 1
                if is_edge and board[y][x] == 'O':
                    dfs(board, y, x)

        for y in range(height):
            for x in range(width):
                if board[y][x] == 'O':
                    board[y][x] = 'X'
                if board[y][x] == '#':
                    board[y][x] = 'O'

        for y in range(height):
            print(board[y])


if __name__ == '__main__':
    Solution().solve([['X', 'X', 'X', 'X'],
                      ['X', 'O', 'O', 'X'],
                      ['X', 'X', 'O', 'X'],
                      ['X', 'O', 'O', 'X']])
