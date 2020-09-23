package com.issac.study.utils;

public class LogUtils {

	private static final String LOG_FORMAT = "[%s] [%s] >>> %s";

	public static void info(String logPattern, Object... args) {
		System.out.println(String.format(LOG_FORMAT,
				TimeUtils.getTimeStr(System.currentTimeMillis(), TimeUtils.DEFAULT_DATE_FORMAT), "INFO",
				String.format(logPattern, args)));
	}

	public static void error(String logPattern, Object... args) {
		System.err.println(String.format(LOG_FORMAT,
				TimeUtils.getTimeStr(System.currentTimeMillis(), TimeUtils.DEFAULT_DATE_FORMAT), "ERROR",
				String.format(logPattern, args)));
	}

	public static void error(Throwable throwable, String logPattern, Object... args) {
		System.err.println(String.format(LOG_FORMAT,
				TimeUtils.getTimeStr(System.currentTimeMillis(), TimeUtils.DEFAULT_DATE_FORMAT), "ERROR",
				String.format(logPattern, args)));
		throwable.printStackTrace();
	}

}
