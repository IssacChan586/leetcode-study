"""
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

示例：
二叉树：[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

from TreeNode import TreeNode


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        def dfs(root: TreeNode, height: int):
            if root:
                if len(result) <= height:
                    result.append([])
                result[height].append(root.val)
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
    assert [[3], [9, 20], [15, 7]] == Solution().levelOrder(tree1)
