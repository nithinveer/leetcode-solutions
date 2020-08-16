from collections import  defaultdict
class Solution(object):
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if words1 == words2:
            return True
        lst1 = words1
        lst2 = words2
        if len(lst1) != len(lst2):
            return False
        dct = defaultdict(list)
        for tmp in pairs:
            dct[tmp[0]].append(tmp[1])
            # dct[tmp[0]].append(tmp[0])
            dct[tmp[1]].append(tmp[0])
            # dct[tmp[1]].append(tmp[1])
        # print(dct)
        for i in range(len(lst1)):
            flage = False
            if lst1[i] == lst2[i]:
                flage = True
            for each_ in dct[lst2[i]]:
                if lst1[i] == each_ :
                    flage = True
            if not flage:
                return  False
        return True





pairs = [["great","good"],["extraordinary","good"],["well","good"],["wonderful","good"],["excellent","good"],["fine","good"],["nice","good"],["any","one"],["some","one"],["unique","one"],["the","one"],["an","one"],["single","one"],["a","one"],["truck","car"],["wagon","car"],["automobile","car"],["auto","car"],["vehicle","car"],["entertain","have"],["drink","have"],["eat","have"],["take","have"],["fruits","meal"],["brunch","meal"],["breakfast","meal"],["food","meal"],["dinner","meal"],["super","meal"],["lunch","meal"],["possess","own"],["keep","own"],["have","own"],["extremely","very"],["actually","very"],["really","very"],["super","very"]]
words1 = ["a","very","delicious","meal"]
words2 =  ["one","really","delicious","dinner"]
# pairs = [["great", "fine"], ["acting","drama"], ["skills","talent"]]
sol = Solution()
print(sol.areSentencesSimilar(words1,words2,pairs))