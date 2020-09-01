"""
给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。
本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:
给定的有序链表： [-10, -3, 0, 5, 9],
一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：
      0
     / \
   -3   9
   /   /
 -10  5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def get_medium(left: ListNode, right: ListNode) -> ListNode:
            fast = slow = left
            while fast != right and fast.next != right:
                fast = fast.next.next
                slow = slow.next
            return slow

        def build_tree(left: ListNode, right: ListNode) -> TreeNode:
            if left == right:
                return None
            mid = get_medium(left, right)
            root = TreeNode(mid.val)
            root.left = build_tree(left, mid)
            root.right = build_tree(mid.next, right)
            return root

        return build_tree(head, None)


def print_tree(tree: TreeNode):
    if tree is not None:
        print(tree.val)
    if tree.left is not None:
        print_tree(tree.left)
    if tree.right is not None:
        print_tree(tree.right)


if __name__ == '__main__':
    # [-10, -3, 0, 5, 9]
    data1 = ListNode(-10)
    data1.next = ListNode(-3)
    data1.next.next = ListNode(0)
    data1.next.next.next = ListNode(5)
    data1.next.next.next.next = ListNode(9)

    print_tree(Solution().sortedListToBST(data1))
