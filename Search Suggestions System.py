class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        products.sort()
        word_map ={}
        for each_ in products:
            tmp = ''
            for char in each_:
                tmp +=char
                if tmp in word_map:
                    if len(word_map[tmp]) <3 :
                        pmt = word_map[tmp]
                        pmt.append(each_)
                        word_map[tmp] = pmt
                else:
                    pmt = []
                    pmt.append(each_)
                    word_map[tmp] = pmt
        rtn = []
        tmp = ''
        for char in searchWord:
            tmp += char
            if tmp in word_map:
                rtn.append(word_map[tmp])
            else:
                rtn.append([])
        return rtn