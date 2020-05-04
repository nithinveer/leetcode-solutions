class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if matrix is None or not matrix:
            return
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self.dummy_matrix = [[[0,0,0] for p in range(self.cols+1)] for k in range(self.rows+1)]
        print(self.cols,self.rows)
        for i in range(1,self.rows+1) :
            for j in range(1,self.cols+1):
                tmp = [0,0,0]
                print(i,j)
                if i == 0:
                    tmp[1] = matrix[i][j]
                else:
                    tmp[1] = matrix[i-1][j-1] + self.dummy_matrix[i-1][j][1]
                if j == 0:
                    tmp[0] = matrix[i][j]
                else:
                    tmp[0] = matrix[i-1][j-1] + self.dummy_matrix[i][j-1][0]
                if i==0 and j==0 :
                    tmp[2] = matrix[i][j]
                elif i==0 or j==0:
                    if  i ==0 :
                        tmp[2] = matrix[i-1][j-1] + self.dummy_matrix[i][j-1][0]
                    else :
                        tmp[2] = matrix[i-1][j-1] + self.dummy_matrix[i-1][j][1]
                else:
                    tmp[2] = matrix[i-1][j-1] +self.dummy_matrix[i-1][j-1][2] + self.dummy_matrix[i][j-1][0]  + self.dummy_matrix[i-1][j][1]

                self.dummy_matrix[i][j] = tmp
        # print(self.dummy_matrix)
        for i in range(len(self.dummy_matrix)):
            print(self.dummy_matrix[i])

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        # a = (self.dummy_matrix[row1][col1][2])
        # b = (self.dummy_matrix[row1][col2+1][2])
        # c= (self.dummy_matrix[row2+1][col1][2])
        # d = (self.dummy_matrix[row2+1][col2+1][2])
        return (self.dummy_matrix[row2+1][col2+1][2] - self.dummy_matrix[row2+1][col1][2] - self.dummy_matrix[row1][col2+1][2] + self.dummy_matrix[row1][col1][2])




matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]
obj = NumMatrix(matrix)
print(obj.sumRegion(1, 2, 2, 4))