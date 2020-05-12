class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        maz_dict = {}
        for each_ in magazine:
            if each_ not in maz_dict:
                maz_dict[each_] =1
            else:
                maz_dict[each_] +=1
        for each_ in ransomNote:
            if each_ not in maz_dict:
                return False
            else:
                if maz_dict[each_] == 1:
                    maz_dict.pop(each_)
                else:
                    maz_dict[each_] -=1
        return True



sol = Solution()
ransomNote = "aa"
magazine = "ab"
print(sol.canConstruct(ransomNote,magazine))