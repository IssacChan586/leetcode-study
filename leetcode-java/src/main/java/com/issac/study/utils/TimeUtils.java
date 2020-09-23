package com.issac.study.utils;

import java.text.SimpleDateFormat;
import java.util.Date;

public class TimeUtils {

	public static final String DEFAULT_DATE_FORMAT = "yyyy-MM-dd HH:mm:ss";

	public static String getTimeStr(Long timestampMs, String dateFormat) {
		return new SimpleDateFormat(dateFormat).format(timestamp2Date(timestampMs));
	}

	public static Date timestamp2Date(Long seconds) {
		if (seconds == null) {
			return null;
		}
		return new Date(seconds * 1000);
	}

}
