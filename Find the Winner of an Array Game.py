class Solution(object):
    def getWinner(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        mx = max(arr)
        if k >= len(arr):
            return mx
        count = 0
        pivot = arr[0]
        while count <=k and len(arr) > 1:
            if count ==k :
                return pivot
            if pivot == mx:
                return mx
            if arr[0] > arr[1]:
                count +=1
                tmp = arr[1]
                del arr[1]
                arr.append(tmp)

            else:
                pivot = arr[1]
                count =1
                tmp = arr[0]
                arr = arr[1:]
                arr.append(tmp)

            # print(pivot, count,arr)
        return pivot






sol = Solution()
arr =[1,11,22,33,44,55,66,77,88,99]
k = 1000000000
print(sol.getWinner(arr,k))