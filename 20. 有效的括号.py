class Solution:
    def isValid(self, s: str) -> bool:
        length = len(s)
        if length & 1:
            return False
        stack = []
        balanced = True
        for i in range(length):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            else:
                if not stack:
                    balanced = False
                    break
                current_char = stack.pop()
                if current_char == '(' and s[i] != ')':
                    balanced = False
                if current_char == '[' and s[i] != ']':
                    balanced = False
                if current_char == '{' and s[i] != '}':
                    balanced = False
            i += 1
        if balanced and not stack:
            return True
        else:
            return False





if __name__ == '__main__':
    s = Solution()
    print(s.isValid("){"))