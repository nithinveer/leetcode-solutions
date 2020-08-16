from collections import  defaultdict
import heapq
class Solution(object):
    def rearrangeString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        freq = defaultdict(int)
        for e in s:
            freq[e] +=1
        # print(freq)
        tmp = []
        for key in freq:
            tmp.append((-1*freq[key], key))
        # print(tmp)
        heapq.heapify(tmp)
        count = 0
        last = {}
        found = False
        dummy = []
        rtn = ''
        while len(tmp) > 0:
            found = False
            while not found:
                if len(tmp) ==0 and len(dummy) !=0:
                    return ''
                    # for each_ in dummy:
                    #     heapq.heappush(tmp, each_)
                    # dummy = []
                    # found = True
                    # count += 1
                else:
                    poped = heapq.heappop(tmp)
                    # print(poped)

                    if poped[1] in last and abs(last[poped[1]]-count) < k:
                            dummy.append(poped)
                    else:
                        last[poped[1]] = count
                        if poped[0] != -1:

                            dum = (poped[0]+1, poped[1])
                            heapq.heappush(tmp,dum)
                        rtn += poped[1]
                        for each_ in dummy:
                            heapq.heappush(tmp, each_)
                        dummy = []
                        found = True
                        count +=1
            # print(tmp,count, last, poped, dummy)
            # print(rtn, tmp, last, dummy)
        return rtn


sol = Solution()
s = "aaabc"
k = 3
print(sol.rearrangeString(s,k))

