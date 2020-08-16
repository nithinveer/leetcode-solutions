from collections import  defaultdict
import heapq
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        if n==0:
            return len(tasks)
        freq = defaultdict(int)
        for e in tasks:
            freq[e] +=1
        print(freq)
        tmp = []
        for key in freq:
            tmp.append((-1*freq[key], key))
        print(tmp)
        heapq.heapify(tmp)
        count = 0
        last = {}
        found = False
        dummy = []
        while len(tmp) > 0:
            found = False
            while not found:
                if len(tmp) ==0 and len(dummy) !=0:
                    for each_ in dummy:
                        heapq.heappush(tmp, each_)
                    dummy = []
                    found = True
                    count += 1
                    # print("Hi")
                else:
                    poped = heapq.heappop(tmp)

                    if poped[1] in last and abs(last[poped[1]]-count) <= n:
                            dummy.append(poped)
                    else:
                        last[poped[1]] = count
                        if poped[0] != -1:
                            dum = (poped[0]+1, poped[1])
                            heapq.heappush(tmp,dum)
                        for each_ in dummy:
                            heapq.heappush(tmp, each_)
                        dummy = []
                        found = True
                        count +=1
            # print(tmp,count, last, poped, dummy)
        return count




sol = Solution()
tasks = ["A","A","A","B","B","B"]
n = 2
print(sol.leastInterval(tasks,n))