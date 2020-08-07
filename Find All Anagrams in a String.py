class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        s_lst = [0]*26
        p_lst = [0] * 26
        for each in p:
            p_lst[ord(each)-ord('a')] +=1

        # print(p_lst)
        rtn = []
        for index, each in enumerate(s):
            s_lst[ord(each) - ord('a')] += 1
            if len(p) <= index:
                s_lst[ord(s[index-len(p)]) - ord('a')] -=1

            # print(s_lst,p_lst)
            if s_lst == p_lst:
                rtn.append(index-len(p) +1)
        return (rtn)


s= "abab"
p= "ab"
sol = Solution()
print(sol.findAnagrams(s,p))