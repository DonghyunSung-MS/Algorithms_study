# 거리가 직선 도로 갯수
# 방향전환 cnt 코너갯수
# 3차원 배열로 costs 트랙킹하면 풀림

from collections import deque

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

N = None
cost = None
dist_weight = 100
corner_weight = 500
max_int = int(1e+9)

def bfs( board):
    
    cost = [[[max_int for _ in range(4)] for _ in range(N)] for _ in range(N)]
    for i in range(4):
        cost[0][0][i] = 0
            
    distance = 0
    corner_cnt = 0
    before_idx = -1
    
    que = deque([(0, 0, distance, corner_cnt, before_idx)])
    
    result = max_int
    while que:
        cur_x, cur_y, distance, corner_cnt, before_idx = que.popleft()
        running_cost = distance * dist_weight + corner_cnt * corner_weight
        if cur_x == N-1 and cur_y==N-1:
            if result > running_cost:
                result = running_cost
            
        for idx in range(4):
            nx = cur_x + di[idx]
            ny = cur_y + dj[idx]
            
            if 0<=nx<N and 0<=ny<N and board[nx][ny]==0:
                # que에 넣을지 말지 결정               
                next_running_cost = None
                if before_idx == -1 or before_idx==idx:
                    next_running_cost = running_cost + dist_weight
                    if cost[nx][ny][idx] > next_running_cost:
                        cost[nx][ny][idx] = next_running_cost
                        que.append((nx, ny, distance + 1, corner_cnt, idx))
                else:
                    next_running_cost = running_cost + dist_weight + corner_weight
                    if cost[nx][ny][idx] > next_running_cost:
                        cost[nx][ny][idx] = next_running_cost
                        que.append((nx, ny, distance + 1, corner_cnt + 1, idx))

    return result
        

def solution(board):
    global N, cost
    N = len(board)

    result = bfs(board)
    return result

if __name__ == "__main__":
    #K = int(input())
    #board = []
    #for i in range(K):
    #    board.append(list(map(int, input().split())))
    
    #print(K)
    #print(board)
    
    print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
    print("============================")
    print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))
    print("============================")
    print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))
    print("============================")
    print(solution([[0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 1, 1, 0], [1, 0, 0, 1, 0, 0, 0, 0], [1, 1, 0, 0, 0, 1, 1, 1], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 0]]))
    print("============================")
    print(solution([[0,0,0],[0,0,0],[0,0,0]]))
    