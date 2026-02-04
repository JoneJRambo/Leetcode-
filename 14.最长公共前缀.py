from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
            # 以第一个字符串为基准
        first_str = strs[0]

        for i in range(len(first_str)):
            char = first_str[i]
            # 检查其他字符串在相同位置是否有相同字符
            for s in strs[1:]:
                # 如果当前字符串长度不够或字符不匹配
                if i >= len(s) or s[i] != char:
                    return first_str[:i]
        return first_str

if __name__ == '__main__':
    s = Solution()
    strs = ["abc","ab","b","ba"]
    strs1 =['flower','flow','flight']
    strs2=[]
    print(s.longestCommonPrefix(strs))
    print(s.longestCommonPrefix(strs1))
    print(s.longestCommonPrefix(strs2))





