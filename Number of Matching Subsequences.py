from collections import defaultdict
from bisect import bisect_right


class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        source = defaultdict(list)
        for idx, val in enumerate(S):
            source[val].append(idx)
        rtn = 0

        def ismatch(word):
            idx = -1
            for char in word:
                if char not in source:
                    return 0
                idx_lst = source[char]
                match_index = bisect_right(idx_lst, idx)
                if match_index < len(idx_lst):
                    idx = idx_lst[match_index]
                else:
                    return 0
            return 1

        for word in words:
            rtn += ismatch(word)
        return rtn


S = "abcde"
words = ["a", "bb", "acd", "ace"]
sol = Solution()
print(sol.numMatchingSubseq(S, words))