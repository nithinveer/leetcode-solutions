class Solution(object):
    def __init__(self):
        self.mem = {}

    def checkPath(self, sx, sy, tx, ty):
        print(sx, sy, tx, ty)
        if str(sx)+'#'+str(sy) in self. mem:
            return self.mem[str(sx)+'#'+str(sy)]
        if sx > tx or sy > ty:
            res =  False
        elif sx == tx and sy == ty :
            res = True
        else:
            res = self.checkPath(sx+sy,sy, tx, ty) or self.checkPath(sx, sx+sy, tx, ty)

        self.mem[str(sx)+'#'+str(sy)] = res
        return  res

    def reachingPoints(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        """
        return self.checkPath( sx, sy, tx, ty)

sol = Solution()
sx = 1
sy = 1
tx = 2
ty = 2
print(sol.reachingPoints(sx,sy,tx,ty))