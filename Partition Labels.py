def partitionLabels( S):
    rtn_lst = []
    while S:
        last_pos = len(S)  -S[::-1].index(S[0])
        temp_str = S[0:last_pos]
        # print(temp_str)
        travel_set = set()
        travel_set.add(S[0])
        pivot = 0
        while(pivot < len(temp_str)):

            if temp_str[pivot] not in travel_set:
                last_pos = len(S)  -S[::-1].index(temp_str[pivot])
                # print(last_pos)
                if last_pos +1 > len(temp_str):
                    temp_str = S[0:last_pos]
                travel_set.add(temp_str[pivot])

            # print(pivot, temp_str[pivot],temp_str, travel_set)
            pivot += 1
        # print(temp_str)
        rtn_lst.append(len(temp_str))
        S = S[pivot:]
        # print(S)
        # exit(0)
    return rtn_lst





if __name__ == '__main__':
    S = "ababcbacadefegdehijhklij"
    print(partitionLabels(S))