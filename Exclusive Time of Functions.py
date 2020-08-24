class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        rtn = [0]*n
        stack = []
        prev = 0
        for log in logs:
            tmp = log.split(':')
            if tmp[1] == 'start':
                if stack:
                    poped = stack.pop()
                    # print(poped)
                    stack.append((poped[0], poped[1]+int(tmp[2])-prev-1))
                stack.append((int(tmp[0]), 0))
                prev = int(tmp[2])-1
            else:
                poped = stack.pop()
                # print(poped)
                rtn[poped[0]] = poped[1] + int(tmp[2])-prev
                prev = int(tmp[2])
            # print(stack, rtn)
        return rtn






sol = Solution()
n = 3
logs = ["0:start:0","1:start:2","1:end:5","2:start:6","2:end:9", "0:end:12"]
print(sol.exclusiveTime(n,logs))