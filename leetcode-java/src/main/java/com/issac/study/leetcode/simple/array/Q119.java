package com.issac.study.leetcode.simple.array;

import org.testng.annotations.Test;

import java.util.ArrayList;
import java.util.List;

/**
 * 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
 * 在杨辉三角中，每个数是它左上方和右上方的数的和。
 * <p>
 * 示例:
 * 输入: 3
 * 输出: [1,3,3,1]
 * <p>
 * 进阶：
 * 你可以优化你的算法到 O(k) 空间复杂度吗？
 * <p>
 * 来源：力扣（LeetCode）
 * 链接：https://leetcode-cn.com/problems/pascals-triangle-ii
 * 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
 */
public class Q119 {

	@Test
	public void test() {
		System.out.println(new Solution().getRow(0));
		System.out.println(new Solution().getRow(21));
	}

	class Solution {
		public List<Integer> getRow(int rowIndex) {
			List<Integer> ans = new ArrayList<Integer>() {{add(1);}};
			for (int i = 1; i <= rowIndex; i++) {
				ans.add((int) ((long) ans.get(i - 1) * (long) (rowIndex + 1 - i) / i));
			}
			return ans;
		}
	}

}
