class Solution(object):
    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        t_map ={}
        for each_c in T:
            t_map[each_c] = []
        for index, val in enumerate(S):
            if val in t_map:
                temp = t_map[val]
                temp.append(index)
                t_map[val] = temp
        print(t_map)
        for each_start in t_map[T[0]]:
            t_index = 1
            last_start = each_start
            while t_index < len(T):
                temp_+st
                comp_vals = t_map[T[t_index]]
                for each_c in comp_vals:
                    if each_c > last_start:
                        last_start  = each_c
                        break




sol = Solution()
S = "abcdebdde"
T = "bde"
print(sol.minWindow(S,T))