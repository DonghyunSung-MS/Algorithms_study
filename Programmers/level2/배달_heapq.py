import heapq

def solution(N, road, K):
    answer = 0
    
    edges = [[] for _ in range(N+1)]
    cost_dict = [[float("inf") for _ in range(N+1)] for _ in range(N+1)]
    # 1 부터 거리
    for x, y, cost in road:
        edges[x].append(y)
        edges[y].append(x)
        
        cost_dict[x][y] = min(cost_dict[x][y], cost)
        cost_dict[y][x] = min(cost_dict[y][x], cost)
    
        
    
    pri_que = []
    start = 1
    heapq.heappush(pri_que, (0, start))
    
    dist_dp = [float("inf")]*(N+1)
    dist_dp[start] = 0
    
    while pri_que:
        
        cdist, node = heapq.heappop(pri_que)
        # 현재 가장 짧은 거리보다 테이블이 작으면 넘어감
        if dist_dp[node] < cdist:
            continue
        
        for nnode in edges[node]:
            ndist = cdist + cost_dict[nnode][node]
            if ndist< dist_dp[nnode]:
                dist_dp[nnode] = ndist
                heapq.heappush(pri_que, (ndist, nnode))
    
    
    answer = 0
    for i in range(1, N+1):
        if dist_dp[i]<=K:
            answer += 1
    print(dist_dp)
    return answer