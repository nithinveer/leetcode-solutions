class Solution(object):
    def canVisitAllRoomsBDS(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = set()
        visited.add(0)
        tmp_ = rooms[0]
        while len(tmp_) > 0:
            sub_level= []
            for each_ in tmp_:
                visited.add(each_)
                for _each in rooms[each_]:
                    if _each not in visited:
                        # print(_each)
                        visited.add(_each)
                        sub_level.append(_each)
            tmp_ = sub_level
        # print(visited)
        for i in range(len(rooms)):
            if i not in visited:
                return False

        return True


    def __init__(self):
        self.visited = set()
        self.rooms = []

    def dfs(self, node):
        self.visited.add(node)
        for each_ in self.rooms[node]:
            if each_ not in self.visited:
                self.visited.add(each_)
                self.dfs(each_)

    def canVisitAllRooms(self, rooms):
        self.rooms = rooms
        self.visited.add(0)
        for each_ in rooms[0]:
            self.dfs(each_)
        for i in range(len(rooms)):
            if i not in self.visited:
                return False

        return True



sol = Solution()
rooms =[[1],[2],[3],[]]
print(sol.canVisitAllRooms(rooms))