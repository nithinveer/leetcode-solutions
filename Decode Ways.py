class Solution(object):
    def __init__(self):
        self.rtn = []
        self.dct = {}

    def constructed(self, tmp, partial):
        if len(partial) == 0:
            self.rtn.append(tmp)
            return 1
        if int(partial[0]) == 0:
            return 0
        # if len(partial) >= 1:
        #     if len(partial) >1 and int(partial[1]) ==0:
        #         pass
        #     else:
        else:
            if partial not in self.dct :
                sec = 0
                first = self.constructed(tmp+chr(int(partial[0])-1+ord('a')), partial[1:])
                if len(partial) >1 and int(partial[0:2]) < 27:
                    sec = self.constructed(tmp+chr(int(partial[0:2])-1+ord('a')), partial[2:])

                self.dct[partial] = first+sec
            return self.dct[partial]

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # if int(s) !=0 :
        self.constructed('',s)
        print(self.rtn)
        if len(self.rtn) >0:
            print(self.dct[s])
            return self.dct[s]
        else:
            return 0
        # else:
        #     return 0




sol = Solution()
# s = "9371597631128776948387197132267188677349946742344217846154932859125134924241649584251978418763151253"
s = '0'
print(sol.numDecodings(s))