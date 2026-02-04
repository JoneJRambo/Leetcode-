class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        left = 1
        right = num // 2
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == num:
                return True
            elif mid * mid > num:
                right = mid - 1
            else:
                left = mid + 1
        return False

if __name__ == '__main__':
    s = Solution()
    print(s.isPerfectSquare(16))
    print(s.isPerfectSquare(14))
    print(s.isPerfectSquare(134556))