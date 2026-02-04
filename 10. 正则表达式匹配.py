class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s) + 1, len(p) + 1
        dp = [[False] * n for _ in range(m)]
        dp[0][0] = True
        # 初始化首行
        for j in range(2, n, 2):
            dp[0][j] = dp[0][j - 2] and p[j - 1] == '*'
        # 状态转移
        for i in range(1, m):
            for j in range(1, n):
                if p[j - 1] == '*':
                    if dp[i][j - 2]:
                        dp[i][j] = True   # 1.第一种情况是 p[j - 1] == '*' 不需要被使用
                    elif dp[i - 1][j] and s[i - 1] == p[j - 2]:
                        dp[i][j] = True   # 2.第二种情况是 p[j - 1] == '*' 用了一次当作字符
                    elif dp[i - 1][j] and p[j - 2] == '.':
                        dp[i][j] = True   # 3.第三种情况是 p[j - 1] == '*' 用了一次当作.去充当字符

                else:
                    if dp[i - 1][j - 1] and s[i - 1] == p[j - 1]:
                        dp[i][j] = True   # 1. s上的字符和p上的字符直接相等了
                    elif dp[i - 1][j - 1] and p[j - 1] == '.':
                        dp[i][j] = True   # 2. p上是一个.能够充当字符
        return dp[-1][-1]