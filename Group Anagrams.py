def groupAnagrams( strs):
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




if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(groupAnagrams(strs))