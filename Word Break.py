class Solution(object):
    def __init__(self):
        self.found = False
        self.memo = {}



    def dfs(self, tmp, idx):
        # print(tmp,idx)
        #base case
        if tmp in self.wordDict and idx == len(self.s)-1:
            print(tmp, idx)
            self.found = True
            return True
        elif idx == len(self.s)-1:
            return False
        if tmp+"#"+str(idx) not in self.memo:
            a = False
            if tmp in self.wordDict:
                print(tmp, idx)
                a = self.dfs(self.s[idx+1], idx+1)
            b = self.dfs(tmp+self.s[idx+1], idx+1)
            self.memo[tmp+"#"+str(idx)] = a or b
        return self.memo[tmp+"#"+str(idx)]
        # return

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        self.wordDict = wordDict
        self.s = s
        self.dfs(s[0],0)
        return self.found

    def wordBreakOld(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False for i in range(len(s) + 1)]
        dp[0] = True
        for i in range(1, len(s) + 1):
            for word in wordDict:
                if dp[i - len(word)] and s[i - len(word):i] == word:
                    dp[i] = True

        return dp[-1]

sol = Solution()
s = "acaaaaabbbdbcccdcdaadcdccacbcccabbbbcdaaaaaadb"


wordDict = ["abbcbda","cbdaaa","b","dadaaad","dccbbbc","dccadd","ccbdbc","bbca","bacbcdd","a","bacb","cbc","adc","c","cbdbcad","cdbab","db","abbcdbd","bcb","bbdab","aa","bcadb","bacbcb","ca","dbdabdb","ccd","acbb","bdc","acbccd","d","cccdcda","dcbd","cbccacd","ac","cca","aaddc","dccac","ccdc","bbbbcda","ba","adbcadb","dca","abd","bdbb","ddadbad","badb","ab","aaaaa","acba","abbb"]
print(sol.wordBreak(s, wordDict))