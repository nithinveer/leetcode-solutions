class Solution(object):
    def findRepeatedDnaSequences(self, s):
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


s =  "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
sol = Solution()
print(sol.findRepeatedDnaSequences(s))