class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        rtn = []
        for each in asteroids:
            if each > 0:
                rtn.append(each)
            else:
                isBroken = False
                while len(rtn) > 0 and not isBroken:
                    if rtn[-1] > 0 and   rtn[-1] <= abs(each):
                        if rtn[-1] == abs(each):
                            isBroken = True
                        rtn.pop()
                    elif rtn[-1] <0:
                        rtn.append(each)
                        isBroken = True
                    else:
                        isBroken = True

                if not isBroken:
                    rtn.append(each)
        return (rtn)


sol = Solution()
asteroids = [5, 10, -5]
print(sol.asteroidCollision(asteroids))
