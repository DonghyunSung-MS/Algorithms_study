import math

def solution(n, stations, w):
    answer = 0
    
    bs = 1
    for s in stations:
        # s - w ~ s + w 
        
        # bs ~ s - w - 1 까지 몇개 필요한지
        # 안되는 시작 ~ 되는 끝
        answer += math.ceil((s - w - bs)/ (2*w+1))
        
        bs = s + w + 1 # 안되는 시작
    
    answer += math.ceil((n + 1 - bs)/ (2*w+1))
        
    
    return answer