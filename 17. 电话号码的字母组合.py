from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict1  = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        if not digits:
            return []
        res = ['']
        for i in digits:
            tmp = []
            for j in res:
                for k in dict1[i]:
                    tmp.append(j + k)
            res = tmp

        return res




if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations('23'))