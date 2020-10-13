package com.issac.study.struct;

public class ListNode {
	public int val;
	public ListNode next;

	public ListNode() {
	}

	public ListNode(int val) {
		this.val = val;
	}

	public ListNode(int val, ListNode next) {
		this.val = val;
		this.next = next;
	}

	public ListNode(int[] valList) {
		this.val = valList[0];
		ListNode curNode = this;
		for (int i = 1; i < valList.length; i++) {
			curNode.next = new ListNode(valList[i]);
			curNode = curNode.next;
		}
	}

	public void printList() {
		System.out.println();
		ListNode curNode = this;
		while (curNode != null) {
			System.out.print(curNode.val);
			if (curNode.next != null) {
				System.out.print("->");
			}
			curNode = curNode.next;
		}
		System.out.println();
	}
}