package com.issac.study.leetcode.medium.math;

import org.testng.Assert;
import org.testng.annotations.Test;

import java.util.Arrays;

public class Q593 {

	@Test
	public void test() {
		Assert.assertTrue(
				new Solution().validSquare(new int[]{0, 0}, new int[]{1, 1}, new int[]{1, 0}, new int[]{0, 1}));
		Assert.assertFalse(
				new Solution().validSquare(new int[]{0, 1}, new int[]{1, 1}, new int[]{1, 0}, new int[]{0, 1}));
		Assert.assertTrue(
				new Solution().validSquare(new int[]{0, 0}, new int[]{0, 0}, new int[]{0, 0}, new int[]{0, 0}));
	}

	class Solution {
		private int squareSum(int[] p1, int[] p2) {
			return (p1[0] - p2[0]) * ((p1[0] - p2[0])) + (p1[1] - p2[1]) * ((p1[1] - p2[1]));
		}

		public boolean validSquare(int[] p1, int[] p2, int[] p3, int[] p4) {
			int[] distanceList = new int[]{squareSum(p1, p2), squareSum(p1, p3), squareSum(p1, p4), squareSum(p2, p3),
					squareSum(p2, p4), squareSum(p3, p4)};
			Arrays.sort(distanceList);
			return distanceList[0] == distanceList[1] && distanceList[1] == distanceList[2]
					&& distanceList[2] == distanceList[3] && distanceList[3] != distanceList[4]
					&& distanceList[4] == distanceList[5] && distanceList[5] - distanceList[0] == distanceList[0];
		}
	}

}
