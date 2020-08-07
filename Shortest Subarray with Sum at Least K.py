class Solution(object):
    def binSearch(self,A, mid, K):
        left = 0
        sum = 0
        for i in range(len(A)):
            sum += A[i]
            if sum <0:
                sum = 0
                left = i+1
                continue
            while left < i and (A[left] < 0 or i-left+1 > mid):
                sum -=A[i]
                left+=1
            if sum >= K:
                return True
        return False
    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """


        low = 0
        high = len(A)
        while  low < high:
            mid = int((high+low)/2)
            if self.binSearch(A,mid,K) :
                high = mid
            else:
                low = mid+1
        if self.binSearch(A, low, K) :
            return low
        return -1


A =[1]
K = 1

sol = Solution()
print(sol.shortestSubarray(A,K))