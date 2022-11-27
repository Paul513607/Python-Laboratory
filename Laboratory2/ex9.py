def get_persons_that_can_not_see(height_matrix):
    result = []
    for i in range(0, len(height_matrix)):
        for j in range(0, len(height_matrix[i])):
            flag = any([height_matrix[k][j] >= height_matrix[i][j] for k in range(i - 1, -1, -1)])
            if flag:
                result.append((i, j))
    return result
