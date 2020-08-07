import heapq
class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str

        :rtype: str
        """
        freq = {}
        for each_ in S:
            if each_ in freq:
                freq[each_] -= 1
            else:
                freq[each_] = -1
        cnt = {}
        for key_ in freq.keys():
            if freq[key_] in cnt:
                tmp = cnt[freq[key_]]
            else:
                tmp = []
            tmp.append(key_)
            cnt[freq[key_]] = tmp
        print(cnt, freq)
        heapq.heapify(list(cnt.keys()))
        tmp_ = heapq.heappop(list(cnt.keys()))
        rtn = ''
        print(tmp_)
        tmp_lst = cnt[tmp_]
        rtn+=




sol = Solution()
S = "aab"
print(sol.reorganizeString(S))
