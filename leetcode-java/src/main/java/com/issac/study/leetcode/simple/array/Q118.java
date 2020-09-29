package com.issac.study.leetcode.simple.array;

import com.alibaba.fastjson.JSON;
import org.testng.annotations.Test;

import java.util.ArrayList;
import java.util.List;

/**
 * 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
 * <p>
 * 在杨辉三角中，每个数是它左上方和右上方的数的和。
 * 示例:
 * 输入: 5
 * 输出:
 * [
 * 1: [1]
 * 2: [1, 1]
 * 3: [1, 2,  1]
 * 4: [1, 3,  3,  1]
 * 5: [1, 4,  6,  4, 1]
 * 6: [1, 5, 10, 10, 5,  1]
 * 7: [1, 6, 15, 20, 15, 6, 1]
 * ]
 * <p>
 * 来源：力扣（LeetCode）
 * 链接：https://leetcode-cn.com/problems/pascals-triangle
 * 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
 */
public class Q118 {
	@Test
	public void test() {
		System.out.println(JSON.toJSONString(new Solution().generate(5), true));
	}

	class Solution {
		public List<List<Integer>> generate(int numRows) {
			if (numRows == 0) {
				return new ArrayList<>();
			}
			List<List<Integer>> ans = new ArrayList<List<Integer>>(numRows) {{
				add(new ArrayList<Integer>() {{add(1);}});
			}};
			for (int i = 1; i < numRows; i++) {
				List<Integer> tmpResult = new ArrayList<Integer>() {{ add(1);}};
				for (int j = 1; j < i; j++) {
					tmpResult.add(ans.get(i - 1).get(j) + ans.get(i - 1).get(j - 1));
				}
				tmpResult.add(1);
				ans.add(tmpResult);
			}
			return ans;
		}
	}
}
