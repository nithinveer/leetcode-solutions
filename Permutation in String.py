class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        s2_lst = [0] * 26
        s1_lst = [0] * 26
        for each in s1:
            s1_lst[ord(each) - ord('a')] += 1

        # print(p_lst)
        # rtn = []
        for index, each in enumerate(s2):
            s2_lst[ord(each) - ord('a')] += 1
            if len(s1) <= index:
                s2_lst[ord(s2[index - len(s1)]) - ord('a')] -= 1

            # print(s_lst,p_lst)
            if s2_lst == s1_lst:
                return True
        return False



sol = Solution()
s1 = "ab"
s2 = "eidboaoo"
print(sol.checkInclusion(s1,s2))