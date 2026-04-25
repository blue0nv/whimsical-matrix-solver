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


def cramer(matrix):
    if matrix == None:
        return None

    detA = (
        matrix[0][0] * ((matrix[1][1] * matrix[2][2]) - (matrix[1][2] * matrix[2][1]))
        - matrix[0][1] * ((matrix[1][0] * matrix[2][2]) - (matrix[1][2] * matrix[2][0]))
        + matrix[0][2] * ((matrix[1][0] * matrix[2][1]) - (matrix[1][1] * matrix[2][0]))
    )

    if detA == 0:
        return None

    detA1 = (
        matrix[0][3] * ((matrix[1][1] * matrix[2][2]) - (matrix[1][2] * matrix[2][1]))
        - matrix[0][1] * ((matrix[1][3] * matrix[2][2]) - (matrix[1][2] * matrix[2][3]))
        + matrix[0][2] * ((matrix[1][3] * matrix[2][1]) - (matrix[1][1] * matrix[2][3]))
    )

    detA2 = (
        matrix[0][0] * ((matrix[1][3] * matrix[2][2]) - (matrix[1][2] * matrix[2][3]))
        - matrix[0][3] * ((matrix[1][0] * matrix[2][2]) - (matrix[1][2] * matrix[2][0]))
        + matrix[0][2] * ((matrix[1][0] * matrix[2][3]) - (matrix[1][3] * matrix[2][0]))
    )

    detA3 = (
        matrix[0][0] * ((matrix[1][1] * matrix[2][3]) - (matrix[1][3] * matrix[2][1]))
        - matrix[0][1] * ((matrix[1][0] * matrix[2][3]) - (matrix[1][3] * matrix[2][0]))
        + matrix[0][3] * ((matrix[1][0] * matrix[2][1]) - (matrix[1][1] * matrix[2][0]))
    )

    x1 = detA1 / detA
    x2 = detA2 / detA
    x3 = detA3 / detA

    x = [x1, x2, x3]
    return x


def gauss_jordan(matrix):
    if matrix is None:
        return None

    n = 3

    for i in range(n):
        if matrix[i][i] == 0:
            return None

        pivot = matrix[i][i]

        for j in range(n + 1):
            matrix[i][j] /= pivot

        for k in range(n):
            if k != i:
                factor = matrix[k][i]
                for j in range(n + 1):
                    matrix[k][j] -= factor * matrix[i][j]

    return [matrix[i][n] for i in range(n)]


def lu(matrix):
    if matrix is None:
        return None
    n = 3
    A = [row[:3] for row in matrix]
    b = [row[3] for row in matrix]
    L = [[0]*n for _ in range(n)]
    U = [[0]*n for _ in range(n)]
    for i in range(n):
        for k in range(i, n):
            U[i][k] = A[i][k]
            for j in range(i):
                U[i][k] -= L[i][j] * U[j][k]
        for k in range(i, n):
            if i == k:
                L[i][i] = 1
            else:
                if U[i][i] == 0:
                    return None
                L[k][i] = A[k][i]
                for j in range(i):
                    L[k][i] -= L[k][j] * U[j][i]
                L[k][i] /= U[i][i]
    y = [0]*n
    for i in range(n):
        y[i] = b[i]
        for j in range(i):
            y[i] -= L[i][j] * y[j]
    x = [0]*n
    for i in range(n-1, -1, -1):
        x[i] = y[i]
        for j in range(i+1, n):
            x[i] -= U[i][j] * x[j]
        if U[i][i] == 0:
            return None
        x[i] /= U[i][i]
    return x
