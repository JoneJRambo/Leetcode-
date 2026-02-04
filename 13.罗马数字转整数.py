class Solution:
    def romanToInt(self, s: str) -> int:
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0  # 存储最终结果
        # 从左到右遍历罗马数字字符串
        for i in range(len(s)):
            # 获取当前字符对应的数值
            current_value = roman_values[s[i]]
            if i + 1 < len(s) and current_value < roman_values[s[i + 1]]:
                # 先减再加
                total -= current_value
            else:
                # 末尾也能加
                total += current_value
        return total

if __name__ == '__main__':
    s = Solution()
    str1 ='MDCMDCLXC'
    print(s.romanToInt(str1))