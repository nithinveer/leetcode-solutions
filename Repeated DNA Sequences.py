class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        print(len(s))
        found_dna = set()
        rtn_dna = set()

        for i in range(len(s)-9):
            if s[i:i+10] in found_dna:
                rtn_dna.add(s[i:i+10])
            else:
                found_dna.add(s[i:i+10])

        return(list(rtn_dna))


s = "AAAAAAAAAAA"
sol = Solution()
print(sol.findRepeatedDnaSequences(s))