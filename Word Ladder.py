class Solution(object):
    def compareWords(self, a, b):
        count = 0
        for i in range(len(a)):
            if a[i] == b[i]:
                count +=1
        return count
    def xplore(self, dict_map, start,end,cnt, xplored_lst):
        xplored_lst.append(start)
        for each_word in dict_map[start]:
            if each_word not in xplored_lst:
                if each_word == end:
                    return xplored_lst
                xplored_lst = self.xplore(dict_map, each_word, end,cnt, xplored_lst)
        return xplored_lst


    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        if len(beginWord) != len(endWord):
            return 0
        start_words = []
        for each_word in wordList:
            if self.compareWords(beginWord, each_word) == len(beginWord) - 1:
                start_words.append(each_word)
        print(start_words)
        if len(start_words) == 0:
            return 0
        word_len = len(beginWord)
        dict_pred = {}
        for i in range(len(wordList)-1):
            for j in range(i+1,len(wordList)):
                if self.compareWords(wordList[i], wordList[j]) ==len(endWord)-1:
                    if wordList[i] not in dict_pred:
                        temp = []
                        temp.append(wordList[j])
                        dict_pred[wordList[i]] = temp
                    else:
                        temp = dict_pred[wordList[i]]
                        temp.append(wordList[j])
                        dict_pred[wordList[i]] = temp
                    if wordList[j] not in dict_pred:
                        temp = []
                        temp.append(wordList[i])
                        dict_pred[wordList[j]] = temp
                    else:
                        temp = dict_pred[wordList[j]]
                        temp.append(wordList[i])
                        dict_pred[wordList[j]] = temp

        print(dict_pred)
        rtn_val = float('INF')
        for each_start_word in start_words:
            xplored_lst = []
            cnt = 0
            cnt = len(self.xplore(dict_pred, each_start_word, endWord,cnt, xplored_lst))
            if cnt < rtn_val:
                rtn_val = cnt

        if beginWord in wordList:
            rtn_val +=1
        return rtn_val

beginWord = "hot"
endWord = "dog"
wordList = ["hot","cog","dog","tot","hog","hop","pot","dot"]
sol = Solution()
print(sol.ladderLength(beginWord, endWord, wordList))