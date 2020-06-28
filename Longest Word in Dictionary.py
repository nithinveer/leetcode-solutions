class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        wrd ={}
        for each_ in words:
            if len(each_) in wrd:
                tmp = wrd[len(each_)]
                tmp.append(each_)
                tmp.sort()
                wrd[len(each_)] = tmp
            else:
                tmp = []
                tmp.append(each_)
                wrd[len(each_)] = tmp

        print(wrd)
        rtn = ''
        pivot = 1
        while True:
            # print(pivot)
            tmp = []
            for each_ in wrd[pivot]:

                for i in range(ord('a'), ord('a')+26):
                    # print(each_+chr(i))
                    if pivot+1 in wrd and each_+chr(i) in wrd[pivot+1]:
                        tmp.append(each_+chr(i))

                # print(len(tmp))
            if len(tmp) > 0:
                wrd[pivot+1] = tmp
            else:
                # print("Hello")
                return wrd[pivot][0]
            pivot +=1
            print(wrd)



        # if 1 not in wrd:
        #     return ''
        # for each_ in wrd[1]:




words = ["m","mo","moc","moch","mocha","l","la","lat","latt","latte","c","ca","cat"]
sol = Solution()
print(sol.longestWord(words))