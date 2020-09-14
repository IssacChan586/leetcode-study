"""
给定一个二维网格和一个单词，找出该单词是否存在于网格中。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

示例:
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

给定 word = "ABCCED", 返回 true
给定 word = "SEE", 返回 true
给定 word = "ABCB", 返回 false

提示：
board 和 word 中只包含大写和小写英文字母。
1 <= board.length <= 200
1 <= board[i].length <= 200
1 <= word.length <= 10^3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-search
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(x, y, cur_idx=0) -> bool:
            if cur_idx == len_word - 1:
                return True
            for dir in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                next_x, next_y = x + dir[0], y + dir[1]
                if not (0 <= next_x < width and 0 <= next_y < height):
                    continue
                if board[next_y][next_x] != word[cur_idx + 1]:
                    continue
                origin_char = board[y][x]
                board[y][x] = '#'
                if dfs(next_x, next_y, cur_idx + 1):
                    return True
                board[y][x] = origin_char
            return False

        len_word, height, width = len(word), len(board), len(board[0])
        for y in range(height):
            for x in range(width):
                if board[y][x] == word[0]:
                    if dfs(x, y):
                        return True
        return False


if __name__ == '__main__':
    assert Solution().exist([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], "ABCCED")
    assert Solution().exist([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], "SEE")
    assert not Solution().exist([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], "ABCB")
    assert not Solution().exist([["a", "b"], ["c", "d"]], "abcd")
    assert not Solution().exist([["a"]], "ab")
