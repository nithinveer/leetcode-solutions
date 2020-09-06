class Solution(object):
    def longestArithSeqLength(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        dct = {}
        rtn = 0
        for i in range(0, len(A)-1):
            for j in range(i+1, len(A)):
                diff = A[i] - A[j]
                key = str(i) + '#' +str(A[i]) + '#' + str(diff)
                # print(A[i], A[j], diff)
                val = 2
                if key in dct :
                    val = dct[key]+1
                dct[str(j) + '#' +str(A[j]) + '#' + str(diff)] = val
                if rtn < val:
                    print(str(j) + '#' +str(A[i]) + '#' + str(diff), val)
                rtn = max(rtn, val)
        # print(dct)
        return rtn



A =  [12,28,13,6,34,36,53,24,29,2,23,0,22,25,53,34,23,50,35,43,53,11,48,56,44,53,31,6,
      31,57,46,6,17,42,48,28,5,24,0,14,43,12,21,6,30,37,16,56,19,45,51,10,22,38,39,23,8,29,60,18]
sol = Solution()
print(sol.longestArithSeqLength(A))