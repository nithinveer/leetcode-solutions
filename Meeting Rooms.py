def canAttendMeetings( intervals):
    intervals.sort(key = lambda x: x[0])
    rtn_list = []
    while  len(intervals) > 1:
        if intervals[0][1] > intervals[1][0]:
            return False

        else:
            rtn_list.append(intervals[0])
            intervals.pop(0)
    return  True












if __name__ == '__main__':
    intervals = [[1,4],[0,2],[3,5]]
    print(canAttendMeetings(intervals))