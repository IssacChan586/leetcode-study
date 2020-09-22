package com.issac.study.leetcode.simple;

import org.testng.Assert;
import org.testng.annotations.Test;

/**
 * 给定一个字符串来代表一个学生的出勤记录，这个记录仅包含以下三个字符：
 * <p>
 * 'A' : Absent，缺勤
 * 'L' : Late，迟到
 * 'P' : Present，到场
 * 如果一个学生的出勤记录中不超过一个'A'(缺勤)并且不超过两个连续的'L'(迟到),那么这个学生会被奖赏。
 * <p>
 * 你需要根据这个学生的出勤记录判断他是否会被奖赏。
 * <p>
 * 示例 1:
 * 输入: "PPALLP"
 * 输出: True
 * <p>
 * 示例 2:
 * 输入: "PPALLL"
 * 输出: False
 * <p>
 * 来源：力扣（LeetCode）
 * 链接：https://leetcode-cn.com/problems/student-attendance-record-i
 * 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
 */
public class q551 {

	@Test
	public void test() {
		Assert.assertTrue(new Solution().checkRecord("PPALLP"));
		Assert.assertFalse(new Solution().checkRecord("PPALLL"));
	}

	class Solution {
		public boolean checkRecord(String s) {
			int countA = 0;
			for (int i = 0; i < s.length(); i++) {
				if (s.charAt(i) == 'A') {
					countA++;
				}
				if (countA > 1 || (i > 1 && s.charAt(i) == 'L' && s.charAt(i - 1) == 'L' && s.charAt(i - 2) == 'L')) {
					return false;
				}
			}
			return true;
		}
	}

}
