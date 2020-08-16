class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        dct = {}
        dst = 0
        for e in arr:
            if e in dct:
                dct[e] +=1
            else:
                dct[e] = 1
                dst +=1
        cnt = {}
        for c in dct :
            if dct[c] in cnt:
                tmp = cnt[dct[c]]
            else:
                tmp = []
            tmp.append(c)
            cnt[dct[c]] = tmp
        # print(cnt,dst)
        pivot = 1
        # rtn = 0
        while k >= pivot and len(cnt) > 0 :
            # print(pivot, k)
            if pivot in cnt:
                for e in cnt[pivot] :
                    if k >= pivot:
                        dst -=1
                        k -=pivot
            pivot +=1
        return(dst)



sol = Solution()
arr = [4,3,1,1,3,3,2]
k = 3
print(sol.findLeastNumOfUniqueInts(arr,k))