package com.issac.study.leetcode.simple.tree;

public class Q530 {

	public class TreeNode {
		int val;
		TreeNode left;
		TreeNode right;

		TreeNode(int x) {
			val = x;
		}
	}

	class Solution {
		private int minAbs = Integer.MAX_VALUE;
		private Integer lastValue;

		public void travel(TreeNode root) {
			if (root == null) {
				return;
			}
			travel(root.left);
			if (lastValue == null) {
				lastValue = root.val;
			} else {
				minAbs = Math.min(minAbs, root.val - lastValue);
				lastValue = root.val;
			}
			travel(root.right);
		}

		public int getMinimumDifference(TreeNode root) {
			travel(root);
			return minAbs;
		}
	}

}
