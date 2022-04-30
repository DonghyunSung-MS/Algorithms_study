from itertools import combinations_with_replacement



def solution(n, info):
    answer = [-1]*11
    score = -1
    
    #이기면 추가
    #경우의 수
    candidates = list(combinations_with_replacement(range(11), n)) #n arrow at index
    
    for cand in candidates:
        tmp = [0]*11
        tmp_score = 0
        for index in cand:
            tmp[index] += 1
        
        # compare with info
        for i in range(11):
            if info[i]==0 and tmp[i]==0:
                continue
            
            if info[i] < tmp[i]:
                tmp_score += (10 - i)
            else:
                tmp_score -= (10 - i)
        
        # appeach win
        if tmp_score <=0:
            continue
        
        if tmp_score > score:
            score = tmp_score
            answer = tmp
        
        elif tmp_score == score:
            if answer[::-1] >tmp [::-1]:
                answer = tmp

            
    return answer

if __name__ == "__main__":
    n = 5
    info = [2,1,1,1,0,0,0,0,0,0,0]
    print(solution(n, info))
    