def minMeetingRoomsOld( intervals):
    intervals.sort(key = lambda x: x[0])
    # print(intervals)
    rtn_val = 0
    rtn_list = []
    tmp_val = 0
    while  len(intervals) > 1:
        # print(rtn_list, intervals)
        if intervals[0][1] >= intervals[1][0]:
            if intervals[0][1] >= intervals[1][1]:
                new_ele = [intervals[0][0], intervals[0][1]]
            else:
                new_ele = [intervals[0][0],intervals[1][1]]
            tmp_val +=1
            intervals.pop(0)
            intervals.pop(0)
            intervals.insert(0,new_ele)
        else:
            rtn_list.append(intervals[0])
            intervals.pop(0)
            if tmp_val > rtn_val:
                rtn_val = tmp_val
            tmp_val = 0
        # print(rtn_list, intervals)
    if len(intervals) ==1:
        rtn_list.append(intervals[0])
        intervals.pop(0)
    return  rtn_val

def minMeetingRooms(intervals):
    intervals.sort(key= lambda x:x[0])
    print(intervals)
    end_times = [intervals[0][1]]
    # meet_set= set()
    rtn_val  =1
    for i  in range(1, len(intervals)):
        if intervals[i][0] >= end_times[-1]:
            while(len(end_times)>0 and intervals[i][0] >= end_times[-1]) :
                end_times.pop()
        end_times.append(intervals[i][1])
        end_times.sort(reverse=True)
        if len(end_times) > rtn_val:
            rtn_val = len(end_times)
    return rtn_val





if __name__ == '__main__':
    intervals =[[13,15],[1,13]]
    print(minMeetingRooms(intervals))