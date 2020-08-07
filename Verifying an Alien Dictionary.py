from collections import OrderedDict
class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        dict ={}
        for i in range(26):
            dict[order[i]] = i

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            while word1 or word2:
                if not word1:
                    break
                if not word2:
                    return False
                if dict[word1[0]] < dict[word2[0]]:
                    break
                else:
                    return  False

                word1 = word1[1:]
                word2 = word2[1:]
        return True







words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
sol = Solution()
print(sol.isAlienSorted(words,order))