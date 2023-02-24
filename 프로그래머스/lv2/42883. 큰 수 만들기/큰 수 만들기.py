def solution(number, k):
    stack = []
    
    for num in number:
        # k가 0보다 크고, 스택이 비어있지 않으며, 스택의 마지막 숫자가 num보다 작으면 갈아 끼워 준다. (제거 한다)
        while k > 0 and len(stack) > 0 and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)
        
    slice_len = len(number) - k
    
    # 스택에 남아있는 값은 보다 작은수를 전부 제외한 리스트이다.
    return "".join(stack[:slice_len])