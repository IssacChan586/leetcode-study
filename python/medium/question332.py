"""
给定一个机票的字符串二维数组 [from, to]，子数组中的两个成员分别表示飞机出发和降落的机场地点，对该行程进行重新规划排序。所有这些机票都属于一个从 JFK（肯尼迪国际机场）出发的先生，所以该行程必须从 JFK 开始。
说明:
如果存在多种有效的行程，你可以按字符自然排序返回最小的行程组合。例如，行程 ["JFK", "LGA"] 与 ["JFK", "LGB"] 相比就更小，排序更靠前
所有的机场都用三个大写字母表示（机场代码）。
假定所有机票至少存在一种合理的行程。

示例 1:
输入: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
输出: ["JFK", "MUC", "LHR", "SFO", "SJC"]

示例 2:
输入: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
输出: ["JFK","ATL","JFK","SFO","ATL","SFO"]
解释: 另一种有效的行程是["JFK","SFO","ATL","JFK","ATL","SFO"]。但是它自然排序更大更靠后。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reconstruct-itinerary
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class GraphNode:
    def __init__(self, airport):
        self.cur_airport = airport
        self.next_airport = []


class Solution:

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        airport_map = {}
        for ticket in tickets:
            if ticket[0] not in airport_map:
                airport_map[ticket[0]] = GraphNode(ticket[0])
            if ticket[1] not in airport_map:
                airport_map[ticket[1]] = GraphNode(ticket[1])
            if airport_map[ticket[1]] not in airport_map[ticket[0]].next_airport:
                airport_map[ticket[0]].next_airport.append(airport_map[ticket[1]])
        return None


if __name__ == '__main__':
    assert ["JFK", "MUC", "LHR", "SFO", "SJC"] == Solution().findItinerary(
        [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]])
    assert ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"] == Solution().findItinerary(
        [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]])
