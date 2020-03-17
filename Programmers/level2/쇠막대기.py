def solution(arrangement):
    answer = 0
    stack_list = []
    last = -1
    for ele in arrangement:
        if ele=='(':
            stack_list.append(ele)
            last = ele
        else:
            stack_list.pop()
            if last=='(': #laser    
                answer+=len(stack_list)
            else: #beam
                answer+=1
            last = ele
    return answer
