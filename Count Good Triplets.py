class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        """
        :type arr: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        n = len(arr)
        rtn = 0
        for i in range(0, n):
            for j in range(i+1, n):
                for k in range(j+1,n):
                    if abs(arr[i]-arr[j]) <= a and abs(arr[j]-arr[k])<=b and abs(arr[k]-arr[i]) <=c:
                        rtn+=1

        return rtn




sol = Solution()
arr = [1,1,2,2,3]
a = 0
b = 0
c = 1
print(sol.countGoodTriplets(arr, a,b,c))