class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr) < 2:
            return False
        for i in range(len(arr) - 2):
            if arr[i] % 2 == 1 and arr[i + 1] % 2 == 1 and arr[i + 2]% 2 == 1:
                return True
        return False


sol = Solution()
arr = [1,2,34,3,4,5,7,23,12]
print(sol.threeConsecutiveOdds(arr))