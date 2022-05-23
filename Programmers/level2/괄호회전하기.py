from collections import deque

pairs = {
    "(":")",
    "{":"}",
    "[":"]",
    ")":None,
    "}":None,
    "]":None,
    
}

def isvalid(dq):
    stack = []
    for i in range(len(dq)):
        if len(stack)==0:
            stack.append(dq[i])
            continue
        
        if pairs[stack[-1]]==dq[i]:
            stack.pop()
        
        else:
            stack.append(dq[i])
    
    if len(stack)==0:
        return True
    else:
        return False   


def solution(s):
    answer = 0
    dq = deque(list(s))
    for _ in range(len(s)):
        dq.append(dq.popleft())
        if isvalid(dq):
            answer +=1
        
    return answer