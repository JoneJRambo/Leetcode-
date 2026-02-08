class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        max_length = 1
        left,flag = 0, 0
        for right in range(1,len(s)):
            flag += s[right] == s[right - 1]
            if flag > 1:
                left += 1
                while s[left] != s[left - 1]:
                    left += 1
                flag = 1
            max_length = max(max_length, right - left + 1)

        return max_length

if __name__ == '__main__':
    s = Solution()
    print(s.longestSemiRepetitiveSubstring("52233"))
    print(s.longestSemiRepetitiveSubstring("0001"))
    print(s.longestSemiRepetitiveSubstring("4411794"))