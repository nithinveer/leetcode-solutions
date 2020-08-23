from collections import defaultdict, deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if len(beginWord) != len(endWord) or endWord == beginWord  :
            return 0
        dct = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                dct[word[:i]+'*'+word[i+1:]].append(word)
        # print(dct)

        queue = deque([(beginWord,1)])
        parsed = set()
        parsed.add(beginWord)
        while  queue:
            word, length = queue.popleft()
            for i in range(len(word)):
                tmp = word[:i]+'*'+word[i+1:]
                for each in dct[tmp]:
                    if each == endWord:
                        return length+1
                    if each not in parsed:
                        parsed.add(each)
                        queue.append((each, length+1))
        return 0







beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
sol = Solution()
print(sol.ladderLength(beginWord, endWord, wordList))