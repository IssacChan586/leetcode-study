"""
你有一个日志数组 logs。每条日志都是以空格分隔的字串。
对于每条日志，其第一个字为字母与数字混合的 标识符 ，除标识符之外的所有字为这一条日志的内容.
    除标识符之外，所有字均由小写字母组成的，称为 字母日志
    除标识符之外，所有字均由数字组成的，称为 数字日志

题目所用数据保证每个日志在其标识符后面至少有一个字。

请按下述规则将日志重新排序：
    所有 字母日志 都排在 数字日志 之前。
    字母日志 在内容不同时，忽略标识符后，按内容字母顺序排序；在内容相同时，按标识符排序；
    数字日志 应该按原来的顺序排列。
返回日志的最终顺序。

示例 ：
输入：["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
输出：["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
 
提示：
0 <= logs.length <= 100
3 <= logs[i].length <= 100
logs[i] 保证有一个标识符，并且标识符后面有一个字。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reorder-data-in-log-files
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def reorderLogFiles(self, logs):
        def f(log):
            id_, rest = log.split(" ", 1)
            return (0, rest, id_) if rest[0].isalpha() else (1,)

        return sorted(logs, key=f)

    def reorderLogFilesV2(self, logs: List[str]) -> List[str]:
        char_logs, digit_log = [], []
        for log in logs:
            if log.split()[1][0].isdigit():
                digit_log.append(log)
            else:
                log_pre, log_last = log.split(" ", 1)
                flag = False
                for i in range(len(char_logs)):
                    pre, last = char_logs[i].split(" ", 1)
                    if log_last == last:
                        if pre < log_pre:
                            char_logs.insert(i + 1, log)
                        else:
                            char_logs.insert(i, log)
                        flag = True
                        break
                    elif log_last < last:
                        char_logs.insert(i, log)
                        flag = True
                        break
                if not flag:
                    char_logs.append(log)
        return char_logs + digit_log


if __name__ == '__main__':
    assert Solution().reorderLogFiles(
        ["a1 9 2 3 1", "g1 act car", "f1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]) \
           == ["f1 act car", "g1 act car", "a8 act zoo", "ab1 off key dog", "a1 9 2 3 1", "zo4 4 7"]
