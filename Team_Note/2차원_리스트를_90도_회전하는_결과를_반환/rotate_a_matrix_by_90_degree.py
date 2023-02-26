def rotate_a_matrix_by_90_degree(a):
    n = len(a)  # 행 길이 계산
    m = len(a[0])  # 열 길이 계산
    result = [[0] * n for _ in range(m)]  # 결과 리스트 (열 * 행)
    # print(result)

    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]
            print(i, j, n - i - 1, result)

    return result
