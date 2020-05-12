def groupAnagramsOld( strs):
    rtn_map = {}
    for each_str in strs:
        s_str = ''.join(sorted(each_str))
        if s_str not in rtn_map:
            temp = []
            temp.append(each_str)
            rtn_map[s_str] = temp
        else:
            temp = rtn_map[s_str]
            temp.append(each_str)
            rtn_map[s_str] = temp
    # print(rtn_map)
    return (list(rtn_map.values()))


class Solution(object):
    def groupAnagrams(self, strs):
        listPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83,
                      89, 97, 101, 103]
        grp ={}
        for each_ in strs:
            tmp_ = 1
            for char_ in each_:
                tmp_ = tmp_*(listPrimes[ord(char_) - ord('a')])
            if tmp_ not in grp:
                grp[tmp_] = [each_]
            else:
                lst_tmp = grp[tmp_]
                lst_tmp.append(each_)
                grp[tmp_] = lst_tmp
        return(list(grp.values()))



if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    sol = Solution()
    print(sol.groupAnagrams(strs))