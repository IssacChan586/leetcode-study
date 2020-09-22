"""
给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层次遍历为：

[
  [15,7],
  [9,20],
  [3]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

from python.TreeNode import TreeNode


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        def dfs(root: TreeNode, height: int):
            if root:
                if len(result) <= height:
                    result.insert(0, [])
                result[-height - 1].append(root.val)
                if not root.left and not root.right:
                    return
                dfs(root.left, height + 1)
                dfs(root.right, height + 1)

        result = []
        dfs(root, 0)
        return result


if __name__ == '__main__':
    tree1 = TreeNode(3)
    tree1.left = TreeNode(9)
    tree1.right = TreeNode(20)
    tree1.right.left = TreeNode(15)
    tree1.right.right = TreeNode(7)
    assert [[15, 7], [9, 20], [3]] == Solution().levelOrderBottom(tree1)
