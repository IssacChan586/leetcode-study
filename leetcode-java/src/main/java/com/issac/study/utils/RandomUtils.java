package com.issac.study.utils;

import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.concurrent.ThreadLocalRandom;

public class RandomUtils {

	public static <T> T randomElement(List<T> dataList) {
		if (dataList == null || dataList.size() == 0) {
			return null;
		}
		return dataList.get(new Random().nextInt(dataList.size()));
	}

	public static List<Short> nextShortList(int targetNum, Short min, Short max) {
		List<Short> resultList = new ArrayList<>(targetNum);
		for (int i = 0; i < targetNum; i++) {
			resultList.add(nextShort(min, max));
		}
		return resultList;
	}

	public static List<Byte> nextByteList(int targetNum, Byte min, Byte max) {
		List<Byte> resultList = new ArrayList<>(targetNum);
		for (int i = 0; i < targetNum; i++) {
			resultList.add(nextByte(min, max));
		}
		return resultList;
	}

	public static List<Integer> nextIntegerList(int targetNum, Integer min, Integer max) {
		List<Integer> resultList = new ArrayList<>(targetNum);
		for (int i = 0; i < targetNum; i++) {
			resultList.add(nextInt(min, max));
		}
		return resultList;
	}

	public static List<Long> nextLongList(int targetNum, Long min, Long max) {
		List<Long> resultList = new ArrayList<>(targetNum);
		for (int i = 0; i < targetNum; i++) {
			resultList.add(nextLong(min, max));
		}
		return resultList;
	}

	public static List<Double> nextDoubleList(int targetNum, Double min, Double max) {
		List<Double> resultList = new ArrayList<>(targetNum);
		for (int i = 0; i < targetNum; i++) {
			resultList.add(nextDouble(min, max));
		}
		return resultList;
	}

	public static List<Float> nextFloatList(int targetNum, Float min, Float max) {
		List<Float> resultList = new ArrayList<>(targetNum);
		for (int i = 0; i < targetNum; i++) {
			resultList.add(nextFloat(min, max));
		}
		return resultList;
	}

	public static List<BigDecimal> nextDecimalList(int targetNum, Double min, Double max, int scale,
			RoundingMode roundingMode) {
		List<BigDecimal> resultList = new ArrayList<>(targetNum);
		for (int i = 0; i < targetNum; i++) {
			resultList.add(new BigDecimal(nextDouble(min, max)).setScale(scale, roundingMode));
		}
		return resultList;
	}

	public static short nextShort(short min, short max) {
		return Integer.valueOf(min == max ? min : min + ThreadLocalRandom.current().nextInt(max - min)).shortValue();
	}

	public static byte nextByte(byte min, byte max) {
		return Integer.valueOf(min == max ? min : min + ThreadLocalRandom.current().nextInt(max - min)).byteValue();
	}

	public static int nextInt(int min, int max) {
		return min == max ? min : min + ThreadLocalRandom.current().nextInt(max - min);
	}

	public static long nextLong(long min, long max) {
		return min == max ? min : (long) (min + (max - min) * ThreadLocalRandom.current().nextDouble());
	}

	public static double nextDouble(double min, double max) {
		return Double.compare(min, max) == 0 ? min : min + (max - min) * ThreadLocalRandom.current().nextDouble();
	}

	public static float nextFloat(float min, float max) {
		return Float.compare(min, max) == 0 ? min : min + (max - min) * ThreadLocalRandom.current().nextFloat();
	}

}
