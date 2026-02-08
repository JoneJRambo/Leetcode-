from collections import defaultdict
from typing import Counter


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        max_length = 0
        # cnt = Counter() # hashmap char int
        cnt = defaultdict(int) # defaultdict(int)和Counter()一样
        left = 0
        for right, char in enumerate(s):
            cnt[char] += 1
            while cnt[char] > 2:
                cnt[s[left]] -= 1
                left += 1
            max_length = max(max_length, right - left + 1)
        return max_length



if __name__ == '__main__':
    s = Solution()
    print(s.maximumLengthSubstring("ababcdcd"))