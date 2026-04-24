def matrix_generator(entries):
    matrix = []
    for i in range(3):
        row = []
        for j in range(4):
            num = entries[i][j].get().strip()
            if (num_validator(num)):
                row.append(float(num))
            else:
                return None
        matrix.append(row)
    return matrix


def num_validator(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def gauss(matrix):
    if matrix == None:
        return None
    n = 3
    for i in range(n):
        if matrix[i][i] == 0:
            return None
        for j in range(i + 1, n):
            factor = matrix[j][i] / matrix[i][i]
            for k in range(i, n + 1):
                matrix[j][k] -= factor * matrix[i][k]
    x = [0, 0, 0]
    for i in range(n - 1, -1, -1):
        if matrix[i][i] == 0:
            return None
        x[i] = matrix[i][n]
        for j in range(i + 1, n):
            x[i] -= matrix[i][j] * x[j]
        x[i] /= matrix[i][i]
    return x