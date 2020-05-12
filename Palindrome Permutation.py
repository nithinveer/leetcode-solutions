class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        char_set = set()
        for char in s:
            if char in char_set:
                char_set.remove(char)
            else:
                char_set.add(char)
        if len(char_set) >1:
            return False
        return  True