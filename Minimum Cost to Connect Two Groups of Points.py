class Solution(object):
    def connectTwoGroups(self, cost):
        """
        :type cost: List[List[int]]
        :rtype: int
        """
        row = set()
        col = set()
        rows = len(cost)
        cols = len(cost[0])

        rtn = 0
        for i in range(rows):
            maxi = float('inf')
            for j in range(cols):
                if cost[i][j] < maxi :
                    maxi = cost[i][j]
                    rowCol = j
            rtn += cost[i][rowCol]
            col.add(rowCol)
        # print(rtn, col)
        for j in range(cols):
            if j not in col:
                maxi = float('inf')
                for i in range(rows):
                    if cost[i][j] < maxi:
                        maxi = cost[i][j]

                rtn += maxi
        return rtn




cost = [[93,56,92],
        [53,44,18],
        [86,44,69],
        [54,60,30]]

sol = Solution()
print(sol.connectTwoGroups(cost))