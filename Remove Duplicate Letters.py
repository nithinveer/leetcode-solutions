from collections import defaultdict
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        dct = defaultdict(int)
        
        for i in range(len(s)):
            dct[s[i]] = i
        
        stack = []
        included = set()
        
        for idx in range(len(s)):
            while stack and stack[-1] > s[idx] and dct[stack[-1]] > idx and s[idx] not in included:                
                included.remove(stack[-1])
                stack.pop()
            if s[idx] not in included:
                stack.append(s[idx])
                included.add(s[idx])
        return "".join(e for e in stack)