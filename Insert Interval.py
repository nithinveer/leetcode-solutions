def insert( intervals, newInterval):
    if not intervals:
        return newInterval
    rtn_interval = []
    if newInterval[0] <= intervals[0][0]:
        if newInterval[1] < intervals[0][0]:
            intervals = [newInterval] + intervals
            return intervals
        elif newInterval[1] == intervals[0][0]:
            newInterval[1] = intervals[0][1]
            return [newInterval] + intervals[1:]
        else:
            while len(intervals) > 0 and newInterval[1] >= intervals[0][0]:
                pop_interval  = intervals.pop(0)
                if pop_interval[1] >= newInterval[1]:
                    newInterval[1] = pop_interval[1]
                    return [newInterval] + intervals
            return [newInterval] + intervals
    else:
        while len(intervals)> 0 and newInterval[0] > intervals[0][0]:
            pop_interval = intervals.pop(0)
            if pop_interval[1] <newInterval[0]:
                rtn_interval.append(pop_interval)
            else:
                if pop_interval[1] >= newInterval[1]:
                    newInterval[1] = pop_interval[1]
                newInterval[0] = pop_interval[0]
            print(rtn_interval,newInterval, intervals)
        while len(intervals) >0 and newInterval[1] > intervals[0][1]:
            pop_interval = intervals.pop(0)
        print(rtn_interval, newInterval, intervals)
        if len(intervals) > 0 and newInterval[1] >= intervals[0][0]:
            newInterval[1] = intervals[0][1]
            intervals.pop(0)
        # print(rtn_interval, newInterval, intervals)


        return  rtn_interval + [newInterval] + intervals



if __name__ == '__main__':
    intervals = [[0,0],[1,4],[6,8],[9,11]]
    newInterval = [0,9]
    print(insert(intervals,newInterval))