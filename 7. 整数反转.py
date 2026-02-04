
class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1
        temp = str(x)
        num_str = ''
        sigh = 1
        if temp[0] in '+-':
            sigh = -1 if temp[0] == '-' else 1

        for i in range(len(temp) - 1, -1, -1):
            if temp[i].isdigit():
                num_str += temp[i]

        result = sigh * int(num_str)
        return result if INT_MIN <= result <= INT_MAX else 0

if __name__ == '__main__':
    s = Solution()
    x = 1534236469
    print(s.reverse(x))

