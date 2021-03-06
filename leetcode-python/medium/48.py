"""
给定一个 n×n 的二维矩阵表示一个图像。
将图像顺时针旋转 90 度。
说明：
你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。

示例 1:
给定 matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],
原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

示例 2:
给定 matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],
原地旋转输入矩阵，使其变为:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotate-image
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        len_matrix = len(matrix)
        origin_matrix = [[matrix[i][j] for j in range(len_matrix)] for i in range(len_matrix)]
        for y in range(len_matrix):
            for x in range(len_matrix):
                matrix[y][x] = origin_matrix[len_matrix - x - 1][y]

    def rotateV2(self, matrix: List[List[int]]) -> None:
        matrix[:] = map(list, zip(*matrix[::-1]))


if __name__ == '__main__':
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    Solution().rotate(matrix1)
    assert [[7, 4, 1], [8, 5, 2], [9, 6, 3]] == matrix1

    matrix2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    Solution().rotate(matrix2)
    assert [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]] == matrix2
