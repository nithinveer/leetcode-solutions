from collections import defaultdict
from bisect import bisect_right


class Solution(object):
    def shortestWay(self, source, target):
        """
        :type source: str
        :type target: str
        :rtype: int
        """
        sou = defaultdict(list)
        for idx, val in enumerate(source):
            sou[val].append(idx)
        for t in target:
            if t not in sou:
                return -1

        def ismatch(word):
            idx = -1
            for char in word:
                if char not in sou:
                    return 0
                idx_lst = sou[char]
                match_index = bisect_right(idx_lst, idx)
                if match_index < len(idx_lst):
                    idx = idx_lst[match_index]
                else:
                    return 0
            return 1

        rtn = idx =0
        tmp = ''
        while idx < len(target):
            tmp += target[idx]
            if ismatch(tmp) == 1:
                idx += 1
            else:
                rtn += 1
                tmp = ''
        return rtn + 1


source = "abc"
target = "acdbc"
sol = Solution()
print(sol.shortestWay(source, target))
