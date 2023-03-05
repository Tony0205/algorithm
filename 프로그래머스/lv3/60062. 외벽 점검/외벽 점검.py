from itertools import permutations

def solution(n, weak, dist):
    answer = len(dist) + 1 # 투입해야 하는 최소 친구 수를 구해야 하므로 최대값으로 초기화

    # 취약 지점을 일자로 표현
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)

    # 모든 출발점과 순서에 대한 경우를 확인
    for start in range(length):
        for friends in permutations(dist, len(dist)):
            count = 1 # 투입한 친구 수
            position = weak[start] + friends[count-1] # 해당 친구가 도달할 수 있는 최대 위치
            for i in range(start, start+length):
                if position < weak[i]: # 해당 친구가 점검할 수 없는 취약 지점이면
                    count += 1
                    if count > len(dist): # 모든 친구를 투입해도 점검이 불가능한 경우
                        break
                    position = weak[i] + friends[count-1] # 다음 친구가 도달할 수 있는 최대 위치로 이동
            answer = min(answer, count)
    
    if answer > len(dist):
        return -1
    return answer
