def merge( intervals):
    intervals.sort(key = lambda x: x[0])
    # print(intervals)
    rtn_list = []
    while  len(intervals) > 1:
        # print(rtn_list, intervals)
        if intervals[0][1] >= intervals[1][0]:
            if intervals[0][1] >= intervals[1][1]:
                new_ele = [intervals[0][0], intervals[0][1]]
            else:
                new_ele = [intervals[0][0],intervals[1][1]]
            intervals.pop(0)
            intervals.pop(0)
            intervals.insert(0,new_ele)
        else:
            rtn_list.append(intervals[0])
            intervals.pop(0)
        # print(rtn_list, intervals)
    if len(intervals) ==1:
        rtn_list.append(intervals[0])
        intervals.pop(0)
    return  rtn_list












if __name__ == '__main__':
    intervals = [[1,4],[0,2],[3,5]]
    print(merge(intervals))