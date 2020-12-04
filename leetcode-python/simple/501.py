"""
给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。

假定 BST 有如下定义：

结点左子树中所含结点的值小于等于当前结点的值
结点右子树中所含结点的值大于等于当前结点的值
左子树和右子树都是二叉搜索树
例如：
给定 BST [1,null,2,2],

   1
    \
     2
    /
   2
返回[2].

提示：如果众数超过1个，不需考虑输出顺序

进阶：你可以不使用额外的空间吗？（假设由递归产生的隐式调用栈的开销不被计算在内）

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-mode-in-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        def pre_order(root: TreeNode) -> None:
            nonlocal max_count, ans
            if root:
                if root.val not in count_map:
                    count_map[root.val] = 0
                count_map[root.val] += 1
                if max_count == count_map[root.val]:
                    ans.append(root.val)
                elif max_count < count_map[root.val]:
                    max_count, ans = count_map[root.val], [root.val]
                pre_order(root.left)
                pre_order(root.right)

        max_count, count_map, ans = 0, {}, []
        pre_order(root)
        return ans


if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(1)
    assert Solution().findMode(root) == [1, 2]
