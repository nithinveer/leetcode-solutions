import heapq
from collections import  defaultdict
class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str

        :rtype: str
        """
        freq = defaultdict(int)
        for each_ in S:
            freq[each_] +=1
        tmp = []
        for key in freq:
            tmp.append((-1*freq[key], key))
        heapq.heapify(tmp)
        rtn = ''
        last = ''
        while len(tmp) > 0:
            poped = heapq.heappop(tmp)
            # print(poped)
            if poped[1] != last:
                rtn+=poped[1]
                last = poped[1]
                if poped[0] != -1:
                    # poped[0] +=1
                    dum = (poped[0]+1, poped[1])
                    heapq.heappush(tmp,dum)

            else:
                if len(tmp) == 0:
                    return ''
                pop2 = heapq.heappop(tmp)
                rtn+=pop2[1]
                last = pop2[1]
                if pop2[0] != -1:
                    dum = (pop2[0]+1, pop2[1])
                    heapq.heappush(tmp, dum)
                heapq.heappush(tmp,poped)
        return (rtn)


        # for key_ in freq.keys():
        #     if freq[key_] in cnt:
        #         tmp = cnt[freq[key_]]
        #     else:
        #         tmp = []
        #     tmp.append(key_)
        #     cnt[freq[key_]] = tmp
        # print(cnt, freq)
        # heapq.heapify(list(cnt.keys()))
        # tmp_ = heapq.heappop(list(cnt.keys()))
        # rtn = ''
        # print(tmp_)
        # tmp_lst = cnt[tmp_]
        # rtn+=




sol = Solution()
S = "aabaabc"
print(sol.reorganizeString(S))
