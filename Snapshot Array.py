from collections import  defaultdict
class SnapshotArray(object):

    def __init__(self, length):
        """
        :type length: int
        """

        self.snps = defaultdict(defaultdict)
        self.snap_id = 0

    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self.snps[self.snap_id][index] = val

    def snap(self):
        """
        :rtype: int
        """
        self.snap_id +=1
        return self.snap_id-1

    def get(self, index, snap_id):
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """
        while snap_id not in self.snps:
            snap_id -=1
        if index in self.snps[snap_id]:
            return self.snps[snap_id][index]
        else:
            return 0

sol = SnapshotArray(3)
sol.set(0,5)
print(sol.snap())
sol.set(0,6)
print(sol.get(0,0))
