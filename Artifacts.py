class Solution(object):
    def locations(self,  start, end):
        if start == end :
            return [start]
        elif start[0] != end[0] and start[1] != end[1]:
            return [start, end, start[0]+end[1], end[0]+start[1]]
        elif start[0] == end[0] and  start[1] != end[1]:
            rtn = []
            for i in range(ord(start[1]), ord(end[1])+1):
                rtn.append(start[0]+chr(i))
            return rtn
        else:
            rtn = []
            for i in range(int(start[0]), int(end[0])+1):
                rtn.append(str(i)+start[1])
            return rtn



    def countArtifacts(self, N, Artifacts, Searched):
        dct = {}
        for each in Artifacts.split(','):
            print(each)
            start , end = each. split(' ')
            coords = self.locations(start, end)
            print(coords)
            for each in coords:
                dct[each] = coords
        sear = set(Searched.split())
        print(Searched.split())
        full = 0
        partial = 0
        for each in Searched.split():
            if each in dct and each in sear:
                count = len(dct[each])
                for _each in dct[each]:
                    if _each in sear:
                        sear.remove(_each)
                        count -=1
                if count == 0:
                    full +=1
                else:
                    partial +=1
        return [full, partial]











sol = Solution()
N = 4
Artifacts = '1B 2C,2D 4D'
Searched = '2B 2D 3D 4D'
print(sol.countArtifacts(N, Artifacts, Searched))