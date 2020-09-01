"""
给定一个二叉树，返回它的中序遍历。
示例:
输入: [1,null,2,3]
   1
    \
     2
    /
   3
输出: [1,3,2]
进阶:递归算法很简单，你可以通过迭代算法完成吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-inorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for a binary tree node.
from typing import List

from leetcode.TreeNode import TreeNode


class Solution:

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []

        def inorder(root: TreeNode):
            if root is None:
                return
            if root.left is not None:
                inorder(root.left)
            result.append(root.val)
            if root.right is not None:
                inorder(root.right)

        inorder(root)
        print(result)
        return result


if __name__ == '__main__':
    tree1 = TreeNode(1)
    tree1.right = TreeNode(2)
    tree1.right.left = TreeNode(3)
    assert [1, 3, 2] == Solution().inorderTraversal(tree1)

    tree2 = TreeNode(1)
    tree2.left = TreeNode(2)
    tree2.left.left = TreeNode(3)
    tree2.left.right = TreeNode(4)
    
    tree2.right = TreeNode(5)
    tree2.right.left = TreeNode(6)
    tree2.right.right = TreeNode(7)
    tree2.right.right.left = TreeNode(8)
    assert [3, 2, 4, 1, 6, 5, 8, 7] == Solution().inorderTraversal(tree2)
