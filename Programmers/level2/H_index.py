def solution(citations):
    answer = 0
    citations.sort()
    start = 1
    N = end = len(citations)
    # citations[start] 논문 인용 이상이 N - start 개 있다
    #  citations[start] > N - start
    #  인용수가 편수보다 많다 낮추자 
    #  citations[start] < N - start 면 반대
    
    while start + 1 < end:
        mid = (start+end)//2
        
        if citations[mid] > N - mid:
            end = mid
        else:
            start = mid
    
    print(start, end)
    return end

solution(list(range(10))) # 5 편 2명 # 4편이상 3 3편이상 4명