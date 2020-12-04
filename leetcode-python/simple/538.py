"""
给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)，使得每个节点的值是原来的节点值加上所有大于它的节点值之和。
例如：
输入: 原始二叉搜索树:
              5
            /   \
           2     13

输出: 转换为累加树:
             18
            /   \
          20     13

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/convert-bst-to-greater-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        def dfs(root: TreeNode):
            nonlocal total
            if root:
                dfs(root.right)
                total += root.val
                root.val = total
                dfs(root.left)

        total = 0
        dfs(root)
        return root

    def convertBSTV2(self, root: TreeNode) -> TreeNode:
        def inner_order(root: TreeNode) -> None:
            if not root:
                return
            inner_order(root.left)
            all_node.append(root.val)
            inner_order(root.right)

        def rebuild_tree(root: TreeNode) -> None:
            if not root:
                return
            rebuild_tree(root.left)
            root.val = sum_map[root.val]
            rebuild_tree(root.right)

        if not root:
            return root
        all_node = []
        inner_order(root)
        all_node.sort(reverse=True)
        sum_map = {all_node[0]: all_node[0]}
        for i in range(1, len(all_node)):
            sum_map[all_node[i]] = sum_map[all_node[i - 1]] + all_node[i]
        rebuild_tree(root)
        return root


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(2)
    root.right = TreeNode(13)
    Solution().convertBST(root)
