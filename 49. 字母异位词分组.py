from collections import defaultdict
from typing import List

'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 创建一个默认值为列表的字典
        # 如果访问不存在的键，会自动创建空列表作为值
        h = defaultdict(list)

        # 遍历输入的每个字符串
        for s in strs:
            # 创建一个长度为26的列表，对应26个英文字母
            # 用于统计当前字符串中每个字母出现的次数
            count = [0] * 26

            # 遍历当前字符串的每个字符
            for ch in s:
                # ord(ch)-97：将字符转换为其在字母表中的位置
                # 'a' -> 97-97 = 0, 'b' -> 98-97 = 1, ... 'z' -> 122-97 = 25
                count[ord(ch) - 97] += 1

            # 将列表转换为元组，因为列表不能作为字典的键（不可哈希）
            # 元组是不可变类型，可以作为字典键
            key = tuple(count)

            # 将当前字符串添加到对应键的列表中
            h[key].append(s)

        # 返回字典中所有值（列表）的列表
        return list(h.values())
'''
#更优方案
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = {}  # 使用标准字典代替 defaultdict
        for s in strs:
            # 对字符串进行排序，作为字典的键
            sorted_s = ''.join(sorted(s))
            # 如果没有该键，初始化为空列表
            if sorted_s not in str_dict:
                str_dict[sorted_s] = []
            # 将字符串添加到对应的组中
            str_dict[sorted_s].append(s)
        # print(str_dict)
        return list(str_dict.values())  # 返回字典中所有值（即各个组）


if __name__ == '__main__':
    solution = Solution()
    strs =["eat","tea","tan","ate","nat","bat"]
    res = solution.groupAnagrams(strs)
    print(res)