class Solution(object):
    def minSwaps(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        tmp = [0]* len(grid)
        position = []
        cnt = -1
        for each_ in grid:
            lst = -1
            cnt+=1
            for i in range(len(grid)):
                if each_[i] == 1:
                    lst = i

            if lst !=-1:
                if tmp[lst] !=0:
                    return -1
                else:
                    tmp[lst] = 1
                    position.append(lst)
            else:
                position.append(-1)
        print(tmp, position)

        for i in range(len(grid)):
            if i in position:
                while (position[i] != i) :
                    locate =






sol = Solution()
grid = [[0,0,1],[1,1,0],[1,0,0]]
print(sol.minSwaps(grid))