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
            elif row[first] < row[p] and row[p] < row[second]:
                second = p
        return first,second
    def minFallingPathSum(self, arr):
        """
        :type arr: List[List[int]]
        :rtype: int
        """
        rows = len(arr)
        cols = len(arr[0])
        tmp = arr[0]
        for i in range(1, rows):
            prev = [0] * cols
            first,second = self.getFirstSecondMin(tmp)
            # print(first,tmp[first],second,tmp[second],tmp)
            for j in range(cols):
                if  j == first:
                    prev[j] = arr[i][j] + tmp[second]
                else:
                    prev[j] = arr[i][j] + tmp[first]
            tmp = prev
            # print(tmp)
        return min(tmp)


arr = [ [2,2,1,2,2],
        [2,2,1,2,2],
        [2,2,1,2,2],
        [2,2,1,2,2],
        [2,2,1,2,2]]
sol = Solution()
print(sol.minFallingPathSum(arr))