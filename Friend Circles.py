class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        count = 0
        rows = cols = len(M)

        dirs = [[1,0],[0,1],[-1,0],[0,-1]]
        def dfs(i, j ):
            M[i][j] = 2
            for dir in dirs:
                y = dir[1]+j
                x = dir[0]+i
                if 0<= y< cols and 0<=x<rows and M[dir[0]+i][dir[1]+j] == 1:
                    dfs(dir[0]+i,dir[1]+j )

        for i in range(rows):
            tmp = []
            friends  = set()
            friends.add(i)
            for j in range(cols):
                if M[i][j] == 1:
                    tmp.append(j)
                    M[i][j] = 2
            if len(tmp) > 0:
                count +=1
                while len(tmp) > 0:
                    tmp_ = []
                    for each in tmp:
                        for j in range(cols):
                            if M[each][j] ==1 and j not in friends:
                                tmp_.append(j)
                            M[each][j] = 2
                        friends.add(each)
                    tmp = tmp_

                    
        return count



sol = Solution()
M = [[1,0,0,1],
     [0,1,0,0],
     [0,0,1,1],
     [1,0,1,1]]
print(sol.findCircleNum(M))