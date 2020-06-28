class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) <3:
            return 0
        rtn = 0
        previous = 0
        current = 0
        isStarted = False
        isIncrease = False

        for i in range(1, len(A)):
            if not isStarted:
                if A[i] > A[i-1] :
                    isStarted = True
                    previous = i-1
                    current = i
                    isIncrease = True
            else:
                if isIncrease :
                    if A[i] > A[i-1]:
                        current = i
                    elif A[i] < A[i-1]:
                        current = i
                        isIncrease = False
                    else:
                        # rtn = max(rtn, current-previous)
                        isStarted = False
                else:
                    if A[i] < A[i-1] :
                        current = i
                    elif A[i] > A[i-1] :
                        rtn = max(rtn,current-previous )
                        previous = i-1
                        current = i
                        isIncrease = True
                    else:
                        rtn = max(rtn, current-previous)
                        isStarted = False
            print(i, previous, current, rtn)
        if not isIncrease:
            rtn = max(rtn, current-previous)
        rtn +=1
        if rtn > 2:
            return rtn
        return 0








sol = Solution()
A = [2,2,2]
print(sol.longestMountain(A))