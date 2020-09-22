package com.issac.study.utils;

public class NumberUtils {

	/**
	 * @param num1
	 * @param num2
	 * @return -1: num1 < num2; 0: num1 == num2; 1: num1 > num2
	 */
	public static int compareNumber(Number num1, Number num2) {
		if (num1 instanceof Short) {
			return ((Short) num1).compareTo((Short) num2);
		}
		if (num1 instanceof Byte) {
			return ((Byte) num1).compareTo((Byte) num2);
		}
		if (num1 instanceof Integer) {
			return ((Integer) num1).compareTo((Integer) num2);
		}
		if (num1 instanceof Long) {
			return ((Long) num1).compareTo((Long) num2);
		}
		if (num1 instanceof Double) {
			return ((Double) num1).compareTo((Double) num2);
		}
		if (num1 instanceof Float) {
			return ((Float) num1).compareTo((Float) num2);
		}
		throw new IllegalArgumentException("不支持数据类型");
	}

}
