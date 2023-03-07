import sys

# open_dir = r"C:\Users\cmh02\OneDrive\바탕 화면\Algorithm\python_algorithm\코드_구현력_기르기\04\in1.txt"
# sys.stdin = open(open_dir, "rt")

n = int(input())

data = list(map(int, input().split()))

sum_data = sum(data)

average = round(sum_data / len(data))

# print(average)

min_gap = float('inf')
min_gap_index = -1
for i in range(len(data)):
    d = data[i]
    gap = abs(average - d)

    if gap < min_gap:
        min_gap = gap
        min_gap_index = i

    # 절댓값이 같을 경우 점수가 높은 학생의 번호를 답으로 한다.
    elif gap == min_gap:
        # 점수 비교, 새로운 학생의 점수가 더 높으면 그것으로 대체
        if data[min_gap_index] < d:
            min_gap = gap
            min_gap_index = i
        else:
            # 만약 점수도 같으면... 
            # (학생이 여러명일 경우 학생번호가 빠른 학생을 답으로 한다.)        
            if min_gap_index > i:
                min_gap_index = i
            continue

print(f'{average} {min_gap_index + 1}')
