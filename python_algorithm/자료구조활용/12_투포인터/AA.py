import sys

open_dir = r"C:\Users\cmh02\OneDrive\바탕 화면\Algorithm\python_algorithm\자료구조활용\12_투포인터\in1.txt"
sys.stdin = open(open_dir, "rt")

seq = list(map(int, input().split()))
k = int(input())


def solution(seq, k):
    candidate = []

    sp, ep = 0, 0
    sum_num = seq[sp]

    while ep < len(seq) - 1:
        if sum_num == k:
            candidate.append((sp, ep))
            ep += 1
            # check to out of range
            if ep >= len(seq):
                break            
            sum_num += seq[ep]

        elif (sum_num > k):
            sum_num -= seq[sp]
            sp += 1

        elif (sum_num < k):
            ep += 1
            
            # check to out of range
            if ep >= len(seq):
                break
            sum_num += seq[ep]

    
    candidate.sort(key=lambda x: x[1] - x[0])

    print(candidate)

    return candidate


solution(seq, k)
