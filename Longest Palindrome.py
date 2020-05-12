class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_set = set()
        rtn_cal = 0
        for each_ in s:
            if each_ in char_set:
                rtn_cal += 2
                char_set.remove(each_)
            else:
                char_set.add(each_)
        if len(char_set) > 0:
            return rtn_cal + 1
        return rtn_cal

    def longestPalindromeOld(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_map = {}
        for char_ in s:
            if char_ in char_map:
                char_map[char_] += 1
            else:
                char_map[char_] = 1
        rtn_val = 0
        odd_max = 0
        # print(char_map)
        for each_ in char_map.keys():
            if char_map[each_] % 2 == 0:
                rtn_val += char_map[each_]
                # print(char_map[each_],rtn_val)
            else:
                odd_max = max(odd_max, char_map[each_])
                rtn_val += (char_map[each_] - 1)
        if odd_max > 0:
            return rtn_val + 1
        return rtn_val

sol = Solution()
s = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
print(sol.longestPalindrome(s))