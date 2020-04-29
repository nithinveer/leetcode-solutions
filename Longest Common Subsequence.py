class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        rows = len(text1)
        cols = len(text2)
        matching = [[0 for j in range(rows+1) ]for i in range(cols+1)]
        # print(matching)
        for i in range(1, cols+1):
            for j in range(1, rows+1):
                # print(text2[i-1], text1[j-1],i,j)
                if text2[i-1] == text1[j-1]:
                    matching[i][j] = 1+ matching[i-1][j-1]
                else:
                    matching[i][j] = max( matching[i][j - 1] , matching[i-1][j])

        return (matching[cols][rows])




sol = Solution()
text1 = ""
text2 = ""
print(sol.longestCommonSubsequence(text1,text2))