class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans_left = ans_right = 0

        for i in range(n):
            l = i
            r = i
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 1 > ans_right - ans_left:
                ans_left, ans_right = l + 1, r

        for i in range(n):
            l = i
            r = i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 1 > ans_right - ans_left:
                ans_left, ans_right = l + 1, r
        return s[ans_left:ans_right]

#测试用例
solution = Solution()
s='oisaudfdghhoiaweufghi7uaysdhoisaghasudfh9w8ertyasikdfha;ofl;asdfiiiiiaiiidfiiiidasofi'
print(solution.longestPalindrome(s))

'''
更高效
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        n = len(s)
        for i in range(n):
            start = max(i - len(res) - 1, 0)
            temp = s[start:i+1]
            if temp == temp[::-1]:
                res = temp
            else:
                temp = temp[1:]
                if temp == temp[::-1]:
                    res = temp
        return res
'''