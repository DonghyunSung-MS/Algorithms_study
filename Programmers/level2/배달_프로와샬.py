def solution(N, road, K):
    answer = 0
    
    edges = [[] for _ in range(N+1)]
    dist_dp = [[float("inf")]*(N+1) for _ in range(N+1)]
    for i in range(1, N+1):
        dist_dp[i][i] = 0 # self zero
        
    # 1 부터 거리
    for x, y, cost in road:
        edges[x].append(y)
        edges[y].append(x)
        
        dist_dp[x][y] = min(cost, dist_dp[x][y])
        dist_dp[y][x] = min(cost, dist_dp[y][x])
        

    
    start = 1
    

    
    # O(N^3)
    for way_point in range(1, N+1):
        for start in range(1, N+1):
            for end in range(1, N+1):
                dist_dp[start][end] = min(dist_dp[start][end], dist_dp[start][way_point] + dist_dp[way_point][end])

    
    answer = 0
    for i in range(1, N+1):
        if dist_dp[1][i]<=K:
            answer += 1
    print(dist_dp[1])
    return answer