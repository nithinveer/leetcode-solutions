class Solution(object):
    def __init__(self):
        self.rtn =[]
        self.visited = []
        self.rows = 0
        self.cols = 0


    def checkValidity(self, row,col):
        if row >=0 and row < self.rows and col >=0 and col <self.cols:
            return True
        return False

    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        que = []
        self.visited = [[False for j in range(self.cols)] for i in range(self.rows)]
        self.rtn = [[0 for j in range(self.cols)] for i in range(self.rows)]

        for i in range(self.rows):
            for j in range(self.cols):
                if matrix[i][j] == 0:
                    for each_ in directions:
                        if self.checkValidity(i+each_[0], j+each_[1]) and matrix[i+each_[0]][j+each_[1]] ==1 and   not self.visited[i+each_[0]][j+each_[1]]:
                            que.append((i+each_[0], j+each_[1]))
                            self.rtn[i+each_[0]][j+each_[1]] =1
                            self.visited[i+each_[0]][j+each_[1]] = True
                    self.visited[i][j] = True

        val = 2
        while len(que) >0:
            tmp_q = []
            for pop_ in que:
                for each_ in directions:
                    if self.checkValidity(each_[0]+pop_[0],each_[1]+pop_[1]) and matrix[each_[0]+pop_[0]][each_[1]+pop_[1]] == 1 and  not self.visited[each_[0]+pop_[0]][each_[1]+pop_[1]]:
                        self.rtn[each_[0]+pop_[0]][each_[1]+pop_[1]] = val
                        self.visited[each_[0]+pop_[0]][each_[1]+pop_[1]] = True
                        tmp_q.append((each_[0]+pop_[0],each_[1]+pop_[1]) )
            que= tmp_q
            val+=1

        return self.rtn






matrix = [[0],[0],[0],[0],[0]]

sol = Solution()
print(sol.updateMatrix(matrix))
