from collections import defaultdict, Counter

"""
给定两个字符串 s 和 t，长度分别是 m 和 n，返回 s 中的 最短窗口 子串，
使得该子串包含 t 中的每一个字符（包括重复字符）。如果没有这样的子串，返回空字符串 ""。
测试用例保证答案唯一。
示例 1：
输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"
解释：最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'。
示例 2：
输入：s = "a", t = "a"
输出："a"
解释：整个字符串 s 是最小覆盖子串。
示例 3:
输入: s = "a", t = "aa"
输出: ""
解释: t 中两个字符 'a' 均应包含在 s 的子串中，
因此没有符合条件的子字符串，返回空字符串。
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # cnt = defaultdict(int)
        # for c in t:
        #     cnt[c] += 1
        # min_len = float('inf')
        cnt_s = Counter()
        cnt_t = Counter(t)

        left = 0
        ans_left, ans_right = -1, len(s)
        for right, c in enumerate(s):
            cnt_s[c] += 1
            while cnt_s >= cnt_t:
                if right - left  < ans_right - ans_left:
                    ans_left = left
                    ans_right = right
                cnt_s[s[left]] -= 1
                left += 1

        return s[ans_left:ans_right+1] if ans_left >= 0 else ""








if __name__ == '__main__':
    s = Solution()
    print(s.minWindow("ADOBECODEBANC", "ABC"))









