package com.issac.study.leetcode.medium;

import com.issac.study.struct.ListNode;
import org.testng.annotations.Test;

public class Q24 {

	@Test
	public void test() {
		System.out.println(new Solution().swapPairs(null));
		System.out.println("expect: null");

		new Solution().swapPairs(new ListNode(new int[]{1, 2, 3, 4})).printList();
		System.out.println("expect: 2->1->4->3");

		new Solution().swapPairs(new ListNode(new int[]{1, 2, 4})).printList();
		System.out.println("expect: 2->1->4");

		new Solution().swapPairs(new ListNode(new int[]{1})).printList();
		System.out.println("expect: 1");

		new Solution().swapPairs(new ListNode(new int[]{2, 5, 3, 4, 6, 2, 2})).printList();
		System.out.println("expect: 5->2->4->3->2->6->2");

		new Solution().swapPairs(new ListNode(new int[]{2, 5, 3, 4, 6, 2, 2, 3})).printList();
		System.out.println("expect: 5->2->4->3->2->6->3->2");
	}

	class Solution {
		public ListNode swapPairs(ListNode head) {
			if (head == null || head.next == null) {
				return head;
			}
			ListNode newHead = head.next, lastNode = null;
			while (head != null && head.next != null) {
				ListNode tmp1 = head.next, tmp2 = head.next.next;
				tmp1.next = head;
				head.next = tmp2;
				if (lastNode != null) {
					lastNode.next = tmp1;
				}
				lastNode = head;
				head = head.next;
			}
			return newHead;
		}
	}

}
