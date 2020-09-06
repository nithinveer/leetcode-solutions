class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """

        counter = 0
        queue = []
        x = []
        queue.append(x);
        while (len(queue) > 0):
            x = queue.pop()
            if len(x) == N:
                counter += 1
            else:
                for i in range(1, N + 1):
                    y = x[:]
                    if i not in y:
                        if (i % (len(y) + 1) == 0) or ((1 + len(y)) % i == 0):
                            y.append(i)
                            queue.append(y)
        return counter