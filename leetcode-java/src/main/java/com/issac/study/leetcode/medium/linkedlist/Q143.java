package com.issac.study.leetcode.medium.linkedlist;

import com.issac.study.struct.ListNode;
import org.testng.annotations.Test;

import java.util.ArrayList;
import java.util.List;

public class Q143 {

	@Test
	public void test() {
		ListNode head = new ListNode(new int[]{1, 2, 3, 4});
		new Solution().reorderList(head);
		head.printList();


		head = new ListNode(new int[]{1, 2, 3, 4, 5});
		new Solution().reorderList(head);
		head.printList();

		head = new ListNode(new int[]{1});
		new Solution().reorderList(head);
		head.printList();
	}

	class SolutionV2 {
		public void reorderList(ListNode head) {
			if (head == null) {
				return;
			}
			List<ListNode> list = new ArrayList<ListNode>();
			ListNode node = head;
			while (node != null) {
				list.add(node);
				node = node.next;
			}
			int i = 0, j = list.size() - 1;
			while (i < j) {
				list.get(i).next = list.get(j);
				i++;
				if (i == j) {
					break;
				}
				list.get(j).next = list.get(i);
				j--;
			}
			list.get(i).next = null;
		}
	}

	class Solution {
		public void reorderList(ListNode head) {
			if (head == null || head.next == null) {
				return;
			}

			List<ListNode> nodeList = new ArrayList<>();
			ListNode tmpHead = head;
			while (tmpHead != null) {
				nodeList.add(tmpHead);
				tmpHead = tmpHead.next;
			}

			for (int i = 0; i < nodeList.size() / 2 + 1; i++) {
				if (i > 0) {
					nodeList.get(nodeList.size() - i).next = nodeList.get(i);
				}
				nodeList.get(i).next = nodeList.get(nodeList.size() - i - 1);
			}
			nodeList.get(nodeList.size() / 2).next = null;
		}
	}

}
