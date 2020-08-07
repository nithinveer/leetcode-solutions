class Solution(object):
    def __init__(self):
        self.wr = set()
        self.mx = 0
        self.lst = {}

    def check(self, word):
        # print(word)
        tmp_mx = 0
        for i in range(len(word)):
            tmp_ = word[:i]+ word[i+1:]
            local_mx = 0
            if tmp_  and tmp_ in self.wr:
                local_mx = 1+self.lst[tmp_]
            else:
                local_mx = 1
            tmp_mx = max(tmp_mx,local_mx)
        self.lst[word] = tmp_mx
        self.mx = max(self.mx, tmp_mx)




    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        for each_ in words:
            self.wr.add(each_)
        words.sort(key=len)
        for each_ in words:
            self.check(each_)
        print(self.lst)
        return self.mx






sol = Solution()
words = ["ksqvsyq","ks","kss","czvh","zczpzvdhx","zczpzvh","zczpzvhx","zcpzvh","zczvh","gr","grukmj","ksqvsq","gruj","kssq","ksqsq","grukkmj","grukj","zczpzfvdhx","gru"]
print(sol.longestStrChain(words))