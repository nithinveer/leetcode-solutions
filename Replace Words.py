class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        rtn = []
        dict_set = set(dict)
        wds = sentence.split()
        for each_ in wds:
            tmp = ''
            found = False
            for _each in each_:
                tmp += _each
                if tmp in dict_set:
                    rtn.append(tmp)
                    found = True
                    break
            if not found:
                rtn.append(tmp)
        return " ".join(rtn)




dict = ["cat","bat","rat"]
sentence = "the cattle was rattled by the battery"
sol = Solution()
print(sol.replaceWords(dict,sentence))