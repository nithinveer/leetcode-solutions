from collections import OrderedDict


class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = OrderedDict()
        self.total = 0

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: None
        """
        if self.total > 0:
            tmp_key = next(iter(self.dict))
            while (timestamp - tmp_key) >= 300:
                self.total -= self.dict[tmp_key]
                self.dict.pop(tmp_key)
                if self.total > 0:
                    tmp_key = next(iter(self.dict))
                else:
                    break

        if timestamp in self.dict:
            self.dict[timestamp] += 1
        else:
            self.dict[timestamp] = 1
        self.total += 1

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        if self.total > 0:
            tmp_key = next(iter(self.dict))
            while (timestamp - tmp_key) >= 300:
                self.total -= self.dict[tmp_key]
                self.dict.pop(tmp_key)
                if self.total >0:
                    tmp_key = next(iter(self.dict))
                else:
                    break

        return self.total



sol = HitCounter()
["HitCounter","hit","hit","hit","getHits","getHits","getHits","getHits","getHits","hit","getHits"]
[[],[2],[3],[4],[300],[301],[302],[303],[304],[501],[600]]

print(sol.hit(2))
print(sol.hit(3))
print(sol.hit(4))
print(sol.getHits(300))
print(sol.getHits(301))
print(sol.getHits(302))
print(sol.getHits(303))
print(sol.getHits(304))
print(sol.hit(501))
print(sol.getHits(600))


