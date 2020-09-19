from collections import defaultdict, deque


class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        dct = defaultdict(list)
        for idx, value in enumerate(ppid):
            dct[value].append(pid[idx])
        # print(dct)
        rtn = []
        queue = deque([kill])
        while queue:
            poped = queue.popleft()
            rtn.append(poped)
            for each in dct[poped]:
                queue.append(each)
        return rtn



sol = Solution()

pid = [1, 3, 10, 5]
ppid = [3, 0, 5, 3]
kill = 5

print(sol.killProcess(pid, ppid, kill))
