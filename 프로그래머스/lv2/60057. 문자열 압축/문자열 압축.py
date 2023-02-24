def solution(s):
    answer = len(s)
    
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        count = 1
        # 끊어서 비교
        prev = s[0:step]
        
        for j in range(step, len(s), step):
            compair = s[j:j+step]
            # print("compair", compair)
            
            if prev == compair:
                count += 1
            else:
                compressed += str(count) + prev if count >= 2 else prev
                # 초기화
                prev = compair
                count = 1
        
        compressed += str(count) + prev if count >= 2 else prev
        
        # print(compressed)
        
        answer = min(answer, len(compressed))        
        
    return answer