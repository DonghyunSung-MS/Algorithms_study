def check(answer):
    for x, y, material in answer:
        if material == 0: # 기둥
            # 아래 기둥, 양옆 보 유뮤
            if y == 0 or (x, y - 1, 0) in answer or (x - 1, y, 1) in answer or (x, y, 1) in answer:
                continue
            else:
                return False
        else: # 보
            # 아래 기둥(2개) , 양 옆 보 유뮤
            if (x, y - 1, 0) in answer or (x + 1, y - 1, 0) in answer or (
                    (x - 1, y, 1) in answer and (x + 1, y, 1) in answer):
                continue
            else:
                return False

    return True

def solution(n, build_frame):
    answer = set()
    
    for x, y, material, decision in build_frame:
        cand = (x, y, material)
        
        if decision: # 설치
            answer.add(cand)
            if not check(answer):
                answer.remove(cand)
                                   
        else: # 삭제
            answer.remove(cand)
            if not check(answer):
                answer.add(cand)
            
        
    answer = [list(ans) for ans in answer]
    answer.sort(key=lambda x: (x[0], x[1], x[2]))
    
    return answer