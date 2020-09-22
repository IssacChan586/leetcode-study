"""
在本问题中，有根树指满足以下条件的有向图。该树只有一个根节点，所有其他节点都是该根节点的后继。每一个节点只有一个父节点，除了根节点没有父节点。
输入一个有向图，该图由一个有着N个节点 (节点值不重复1, 2, ..., N) 的树及一条附加的边构成。附加的边的两个顶点包含在1到N中间，这条附加的边不属于树中已存在的边。
结果图是一个以边组成的二维数组。 每一个边 的元素是一对 [u, v]，用以表示有向图中连接顶点 u 和顶点 v 的边，其中 u 是 v 的一个父节点。
返回一条能删除的边，使得剩下的图是有N个节点的有根树。若有多个答案，返回最后出现在给定二维数组的答案。

示例1:
输入: [[1,2], [1,3], [2,3]]
输出: [2,3]
解释: 给定的有向图如下:
  1
 / \
v   v
2-->3

示例 2:
输入: [[1,2], [2,3], [3,4], [4,1], [1,5]]
输出: [4,1]
解释: 给定的有向图如下:
5 <- 1 -> 2
     ^    |
     |    v
     4 <- 3

注意:
二维数组大小的在3到1000范围内。
二维数组中的每个整数在1到N之间，其中 N 是二维数组的大小。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/redundant-connection-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.parent = None
        self.next = set()

    def is_upper(self, target_val: int) -> bool:
        cur = self
        while cur:
            if cur.val == target_val:
                return True
            cur = cur.parent
        return False


# Todo 思路错了
class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        node_map = {}
        for edge in edges:
            if edge[0] not in node_map:
                node_map[edge[0]] = TreeNode(edge[0])
            if edge[1] not in node_map:
                node_map[edge[1]] = TreeNode(edge[1])
            # [1, 2] 代表 1->2
            node_map[edge[0]].next.add(node_map[edge[1]])
            node_map[edge[1]].parent = node_map[edge[0]]

        for edge in edges:
            if node_map[edge[0]].is_upper(node_map[edge[1]].val):
                # edge[0] -> edge[1]
                print(edge)
                return edge


if __name__ == '__main__':
    assert Solution().findRedundantDirectedConnection([[1, 2], [1, 3], [2, 3]]) == [2, 3]
    assert Solution().findRedundantDirectedConnection([[1, 2], [2, 3], [3, 4], [4, 1], [1, 5]]) == [4, 1]
