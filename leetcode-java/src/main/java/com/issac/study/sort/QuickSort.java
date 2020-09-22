package com.issac.study.sort;

import com.issac.study.utils.NumberUtils;

public class QuickSort {

	public static void sort(Number[] toSortList) {
		if (toSortList != null) {
			quickSort(toSortList, 0, toSortList.length - 1);
		}
	}

	private static void quickSort(Number[] valueArr, int left, int right) {
		if (left >= right) {
			return;
		}
		int i = left, j = right;
		Number x = valueArr[i];
		while (i < j) {
			while (i < j && NumberUtils.compareNumber(x, valueArr[j]) <= 0) {
				j--;
			}
			if (i < j) {
				valueArr[i] = valueArr[j];
				i++;
			}

			while (i < j && NumberUtils.compareNumber(x, valueArr[i]) > 0) {
				i++;
			}
			if (i < j) {
				valueArr[j] = valueArr[i];
				j--;
			}
		}
		valueArr[i] = x;
		quickSort(valueArr, left, i - 1);
		quickSort(valueArr, i + 1, right);
	}

}
