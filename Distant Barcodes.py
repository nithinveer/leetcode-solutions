from collections import  defaultdict
from heapq  import  heappop, heappush, heapify
class Solution(object):
    def rearrangeBarcodes(self, barcodes):
        """
        :type barcodes: List[int]
        :rtype: List[int]
        """
        dct = defaultdict(int)
        for each in barcodes:
            dct[each] +=1
        tmp = []
        for key in dct:
            tmp.append((-dct[key], key))
        heapify(tmp)
        # print(tmp)
        rtn = []
        last = ''
        while  tmp:
            val, key  = heappop(tmp)
            # print(val, key, last, rtn)
            if key == last:
                val2, key2 = heappop(tmp)
                heappush(tmp,(val,key))
                rtn.append(key2)
                last = key2
                if val2 <-1:
                    heappush(tmp, ( val2+1, key2))
            else:
                rtn.append(key)
                last = key
                if val <- 1:
                    heappush(tmp,(val+1, key))
        return rtn





barcodes = [1,1,1,1,2,2,3,3]
sol = Solution()
print(sol.rearrangeBarcodes(barcodes))