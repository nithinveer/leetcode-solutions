class Solution(object):
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        rtn = []
        found = False
        for i in range(1, len(A)):
            if A[i] > A[i-1]:
                rtn.append(1)
                found = True
            elif A[i] < A[i-1]:
                rtn.append(-1)
                found = True
            else:
                rtn.append(0)
        print(rtn)
        if len(rtn)==0 or not found:
            return 1
        count = 1
        mx = 0

        for i in range(len(rtn)-1):
            if rtn[i] == 0 :
                count = 1
            elif rtn[i+1] !=0 and rtn[i] != rtn[i+1]:
                count +=1
            else:
                count =1
            mx = max(mx, count)
        return  mx+1






A= [100,100,100]
sol = Solution()
print(sol.maxTurbulenceSize(A))