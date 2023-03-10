# [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
# 2차원 리스트 90도 회전
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


# 자물쇠의 중간 부분이 모두 1인지 확인
def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True


# [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
# [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
def solution(key, lock):
    n = len(lock)
    m = len(key)
    # 자물쇠의 크기를 기존의 3배로 변환
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    # 새로운 자물쇠의 중앙 부분에 기존의 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]

    # 4가지 방향에 대해서 확인
    for rotation in range(4):
        key = rotate_a_matrix_by_90_degree(key)  # 열쇠 회전
        # 1~6열 까지 key를 넣으면서 검사
        for x in range(n * 2):
            # 1~6행 까지 key를 넣으면서 검사
            for y in range(n * 2):
                # 자물쇠에 열쇠를 끼워 넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]
                        print("x, y", x, y, i, j)
                        print("x + i, y + j", x + i, y + j)
                        print(new_lock)

                # 새로운 자물쇠에 열쇠가 정확히 들어맞는지 검사
                if check(new_lock) == True:
                    return True
                # 자물쇠에서 열쇠를 다시 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]

    return False


result = solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],
                  [[1, 1, 1], [1, 1, 0], [1, 0, 1]])

print(result)