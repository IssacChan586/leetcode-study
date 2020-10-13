package com.issac.study.leetcode.medium;

import com.issac.study.struct.ListNode;
import org.testng.annotations.Test;

public class Q82 {

	@Test
	public void test() {
		System.out.println(new Solution().deleteDuplicates(new ListNode(new int[]{1, 1, 2, 2})));
		System.out.println("expect: null");

		new Solution().deleteDuplicates(new ListNode(new int[]{1, 2, 3, 3, 4, 4, 5})).printList();
		System.out.println("expect: 1->2->5");

		new Solution().deleteDuplicates(new ListNode(new int[]{1, 2, 3, 3, 4, 4, 5, 5})).printList();
		System.out.println("expect: 1->2");

		new Solution().deleteDuplicates(new ListNode(new int[]{1, 1, 1, 2, 3})).printList();
		System.out.println("expect: 2->3");
	}

	class Solution {
		public ListNode deleteDuplicates(ListNode head) {
			ListNode curNode = head, lastDiffNode = head;
			while (curNode != null) {
				boolean hasSame = false;
				while (curNode.next != null && curNode.val == curNode.next.val) {
					hasSame = true;
					curNode = curNode.next;
				}
				if (hasSame) {
					if (curNode.val == head.val) {
						head = curNode.next;
					}
					lastDiffNode.next = curNode.next;
				} else {
					lastDiffNode = curNode;
				}
				curNode = curNode.next;
			}
			return head;
		}
	}

}
