class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        inD = [0]* (N+1)
        outD = [0] * (N+1)

        for each in trust:
            inD[each[1]] +=1
            outD[each[0]] +=1

        for i in range(1,N+1):
            if inD[i] == N-1 and outD[i] ==0:
                return i
        return -1







N = 3
trust = [[1,3],[2,3],[3,1]]
sol = Solution()
print(sol.findJudge(N,trust))