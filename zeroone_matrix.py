
class Solution:
    def same_shape_matrix(self, rows, columns, init):
        result = []
        for i in range(rows):
            column = []
            for j in range(columns):
                column.append(init)
            result.append(column)
        return result

    def updateMatrix(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return self.same_shape_matrix(len(matrix), len(matrix[0]), None)
        rows = len(matrix)
        columns = len(matrix[0])
        result = self.same_shape_matrix(rows, columns, None)
        # init
        for i, row in enumerate(matrix):
            for j, column in enumerate(row):
                if matrix[i][j] == 0:
                    result[i][j] = 0

        done = False
        while not done:
            done = True
            for i, row in enumerate(matrix):
                for j, column in enumerate(row):
                    if column == 1:
                        distance = self.search_nearest_distance(i, j, result, rows, columns)
                        if distance:
                            if result[i][j] is None:
                                result[i][j] = distance
                                done = False
                            elif result[i][j] > distance:
                                result[i][j] = distance
                                done = False
        return result

    def search_nearest_distance(self, i, j, matrix, rows, columns):
        up, down, left, right = None, None, None, None
        if i-1 >= 0 and matrix[i-1][j] is not None:
            up = 1 + matrix[i-1][j]
        if i+1 < rows and matrix[i+1][j] is not None:
            down = 1 + matrix[i+1][j]
        if j-1 >= 0 and matrix[i][j-1] is not None:
            left = 1 + matrix[i][j-1]
        if j+1 < columns and matrix[i][j+1] is not None:
            right = 1 + matrix[i][j+1]

        _all = list(filter(None, (up, down, left, right)))
        if len(_all) == 0:
            return None
        else:
            result = min(_all)
            return result
