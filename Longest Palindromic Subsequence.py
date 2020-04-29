class Solution(object):
    def printmat(self,mat):
        for each_n in mat:
            print(each_n)
        print("******")
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        matching = [[0 for i in range(len(s))] for j in range(len(s))]
        for i in range(len(s)):
            matching[i][i] = 1
        # self.printmat(matching)
        for p in range(len(s)):
            i = p
            for j in range(p+1,len(s)):
                print(i,j)
                if s[i] == s[j]:
                    matching[i][j] = matching[i+1][j-1]+2
                else:
                    matching[i][j] = max(matching[i][j-1], matching[i+1][j])
                i+=1
                self.printmat(matching)





s = 'bbbab'
sol = Solution()
print(sol.longestPalindromeSubseq(s))