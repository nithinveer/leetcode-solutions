class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) ==0 :
            return []
        chars = {
            "2" : ['a','b','c'],
            "3": ['d', 'e', 'f'],
            "4": ['g', 'h', 'i'],
            "5": ['j', 'k', 'l'],
            "6": ['m', 'n', 'o'],
            "7": ['p', 'q', 'r','s'],
            "8": ['t', 'u', 'v'],
            "9": ['w', 'x', 'y','z']
        }
        digs = list(digits)
        # print(digs)
        org = chars[digs[0]]
        digs = digs[1:]
        for each_ in digs:
            tmp = []
            itr  = chars[each_]
            for _char in org:
                for char_ in itr:
                    tmp.append(_char+char_)

            org = tmp

        return org






sol = Solution()
digits = '243'
print(sol.letterCombinations(digits))