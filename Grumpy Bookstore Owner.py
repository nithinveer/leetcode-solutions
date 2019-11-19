class Solution(object):
    def maxSatisfied(self, customers, grumpy, X):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type X: int
        :rtype: int
        """
        satisfy = 0
        for i in range(len(grumpy)):
            if grumpy[i] == 0:
                satisfy += customers[i]
                customers[i] =0
        temp_sum = 0
        sum = 0
        for index, val in enumerate(customers):
            temp_sum += val
            if index>=X:
                temp_sum -=customers[index-X]
            sum = max(sum,temp_sum)
        return satisfy+sum




if __name__ == '__main__':
    sol = Solution()
    customers = [10,4]
    grumpy = [0, 1]
    X = 2
    print(sol.maxSatisfied(customers,grumpy,X))