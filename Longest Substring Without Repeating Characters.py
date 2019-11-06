class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sub_str = ''
        max_len = 0
        for each_car in s :
            if each_car not in sub_str:
                sub_str += each_car
                if len(sub_str) > max_len:
                    max_len = len(sub_str)
            else:
                print(sub_str)
                sub_str = sub_str[(sub_str.find(each_car) + 1):len(sub_str)]
                print(sub_str)
                sub_str += each_car
                if len(sub_str) > max_len:
                    max_len = len(sub_str)

        return (max_len)

if __name__ == '__main__':
    s = 'abcabcbb'
    sol = Solution()
    print(sol.lengthOfLongestSubstring(s))