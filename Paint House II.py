class Solution(object):
    def getFirstSecondMin(self, row):
        # print(row)
        if row[0] < row[1]:
            first = 0
            second = 1
        else:
            first = 1
            second =0
        for p in range(2,len(row)):
            if row[p]< row[first]:

                second = first
                first = p
            elif row[first] <= row[p] and row[p] < row[second]:
                second = p
        return first,second

    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        arr = costs
        rows = len(arr)
        cols = len(arr[0])
        tmp = arr[0]
        for i in range(1, rows):
            prev = [0] * cols
            first, second = self.getFirstSecondMin(tmp)
            print(first,tmp[first],second,tmp[second],tmp)
            for j in range(cols):
                if j == first:
                    prev[j] = arr[i][j] + tmp[second]
                else:
                    prev[j] = arr[i][j] + tmp[first]
            tmp = prev
            print(tmp)
        return min(tmp)


costs = [[8,16,12,18,9],
         [19,18,8,2,8],
         [8,5,5,13,4],
         [15,9,3,19,2],
         [8,7,1,8,17],
         [8,2,8,15,5],
         [8,17,1,15,3],
         [8,8,5,5,16],
         [2,2,18,2,9]]
sol = Solution()
print(sol.minCostII(costs))
