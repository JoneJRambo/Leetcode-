class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            if not s[left].isalnum(): # 判断是否是字母或数字
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True

if __name__ == '__main__':
    # s = "A man, a plan, a canal: Panama"
    s = "0P"
    solution = Solution()
    result = solution.isPalindrome(s)
    print(result)
