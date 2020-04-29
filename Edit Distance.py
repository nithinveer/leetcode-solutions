class Solution(object):
    def printMat(self,mat):
        for i in range(0,len(mat)):
            print(mat[i])
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1= len(word1)
        l2 = len(word2)
        matching = [[0 for i in range(l1+1)] for j in range(l2+1)]
        for i in range(l1+1):
            matching[0][i] = i
        for i in range(l2+1):
            matching[i][0] =i
        # matching[0][0] = 0
        # print(matching)
        self.printMat(matching)

        for j in range(1, l2+1):
            for i in range(1,l1+1):
                # print(j, i)
                if word1[i-1] == word2[j-1]:
                    matching[j][i] = matching[j-1][i-1]
                else:
                    # self.printMat(matching)
                    # print(matching[i][j-1])
                    matching[j][i] = min(matching[j-1][i-1],matching[j-1][i],matching[j][i-1]) +1
        self.printMat(matching)

        return (matching[len(matching)-1][len(matching[0])-1])




sol = Solution()
word1 = ""
word2 = "r"
print(sol.minDistance(word1,word2))