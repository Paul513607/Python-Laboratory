def replace_matrix_values_under_main_diagonal(matrix):
    for i in range(0, len(matrix)):
        matrix[i] = [0 if i > j else matrix[i][j] for j in range(0, len(matrix[i]))]
    return matrix
