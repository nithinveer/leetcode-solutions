class Solution(object):
    def findRepeatedDnaSequencesOld(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # print(len(s))
        found_dna = set()
        rtn_dna = set()
        tmp = s[0:10]
        found_dna.add(tmp)
        for i in range(10,len(s)):
            tmp = tmp[1:] + s[i]
            if tmp in found_dna:
                rtn_dna.add(tmp)
            else:
                found_dna.add(tmp)

        return(list(rtn_dna))
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # print(len(s))
        if (s == None or len(s) < 10):
            return []
        tmp = 0
        base_num = 3
        for i in range(10):
            tmp += (ord(s[i])* pow(base_num,i))
        # print(tmp)
        found_dna = set()
        rtn_dna = set()
        # exit(0)

        found_dna.add(tmp)
        for i in range(10,len(s)):
            tmp = int((tmp - ord(s[i-10]))/base_num)  + (ord(s[i] )* pow(base_num,9))
            if tmp in found_dna:
                rtn_dna.add(s[i-9:i+1])
            else:
                found_dna.add(tmp)
        return(list(rtn_dna))



        # # print(len(s))
        # found_dna = set()
        # rtn_dna = set()
        # tmp = s[0:10]
        # found_dna.add(tmp)
        # for i in range(10,len(s)):
        #     tmp = tmp[1:] + s[i]
        #     if tmp in found_dna:
        #         rtn_dna.add(tmp)
        #     else:
        #         found_dna.add(tmp)
        #
        # return(list(rtn_dna))

s =  "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
sol = Solution()
print(sol.findRepeatedDnaSequences(s))