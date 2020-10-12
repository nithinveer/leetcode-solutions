class Solution(object):
    def assignBikes(self, workers, bikes):
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: List[int]
        """
        rtn = [-1]* len(workers)
        distances = []

        for bike_idx , (bike_x, bike_y) in enumerate(bikes):
            for worker_idx , (worker_x, worker_y) in enumerate(workers):
                distance = abs(bike_y-worker_y) + abs(bike_x-worker_x)
                distances.append((distance, worker_idx, bike_idx))
        distances.sort()
        bikes_taken = set()
        for distance, worker_idx, bike_idx in distances:
            if bike_idx not in bikes_taken and rtn[worker_idx] == -1:
                rtn[worker_idx] = bike_idx
                bikes_taken.add(bike_idx)
        return rtn



workers = [[0,0],[1,1],[2,0]]
bikes = [[1,0],[2,2],[2,1]]
sol = Solution()
print(sol.assignBikes(workers, bikes))