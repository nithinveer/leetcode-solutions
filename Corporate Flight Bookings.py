class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        nums = [0] * (n + 1)
        for i in bookings:
            nums[i[0] - 1] += i[2]
            nums[i[1]] -= i[2]
        # print(nums)
        for i in range(1, n):
            nums[i] += nums[i - 1]
        return nums[:-1]



sol = Solution()
bookings = [[1,2,10],[2,3,20],[2,5,25]]
n = 5
print(sol.corpFlightBookings(bookings,n))