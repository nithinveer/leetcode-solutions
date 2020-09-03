class Solution(object):
    def __init__(self):
        self.memo = {}

    def __validate(self, s):
        count = 0
        for each in s:
            if each == '(':
                count += 1
            elif each == ')':
                count -= 1
                if count < 0:
                    return False
        return count == 0

    def __corrupted(self, s):
        left = 0
        right = 0
        for each in s:
            if each == '(':
                left += 1
            elif each == ')':
                if left > 0:
                    left -= 1
                else:
                    right += 1
        return left, right

    def dfs(self, tmp, left, right, idx):
        # print(left, right, idx, tmp)
        if left == right == 0 or idx == len(self.s):
            # print(left, right, idx, tmp)
            tmp += self.s[idx:]
            if self.__validate(tmp):
                return [tmp]
            else:
                return []

        if tmp + '#' + str(idx) + '#' + str(left) + '#' + str(right) not in self.memo:
            rtn = []
            if self.s[idx] == '(':
                if left > 0:
                    rtn.extend(self.dfs(tmp, left - 1, right, idx + 1))
                rtn.extend(self.dfs(tmp + '(', left, right, idx + 1))
            elif self.s[idx] == ')':
                if right > 0:
                    rtn.extend(self.dfs(tmp, left, right - 1, idx + 1))
                rtn.extend(self.dfs(tmp + ')', left, right, idx + 1))
            else:
                rtn.extend(self.dfs(tmp + self.s[idx], left, right, idx + 1))

            self.memo[tmp + '#' + str(idx) + '#' + str(left) + '#' + str(right)] = rtn
        return self.memo[tmp + '#' + str(idx) + '#' + str(left) + '#' + str(right)]

    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        left, right = self.__corrupted(s)
        self.s = s
        rtn = (self.dfs('', left, right, 0))
        rtn = list(dict.fromkeys(rtn))
        return rtn


sol = Solution()
s = "))()(("
print(sol.removeInvalidParentheses(s))
