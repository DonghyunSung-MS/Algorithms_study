# 거리가 직선 도로 갯수
# 방향전환 cnt 코너갯수
# 2번 케이스 무한 루프 해결하는법 무엇일까
# DP 구조?

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

N = None
cost = None
dist_weight = 100
corner_weight = 500
max_int = int(1e+9)
answer = None

def dfs(loc, board, distance, corner_cnt, before_idx):
    global cost, answer
    running_cost = distance * dist_weight + corner_weight * corner_cnt
    if loc[0] == N-1 and loc[1] == N-1:
        if answer > running_cost:# 작으면
            answer = running_cost
        return
       
    for idx in range(4):
        ni = loc[0] + di[idx]
        nj = loc[1] + dj[idx]
        
        # not visited and witin boundary and no block
        if 0<=ni<N and 0<=nj<N and board[ni][nj]==0:
            if before_idx==-1 or before_idx==idx: #straint line or start
                next_running_cost = running_cost + dist_weight
                if cost[ni][nj][idx] > next_running_cost:
                    cost[ni][nj][idx] = next_running_cost
                    dfs((ni, nj), board, distance + 1, corner_cnt, idx)
                else:
                    return
                
            else:
                next_running_cost = running_cost + dist_weight + corner_weight
                if cost[ni][nj][idx] > next_running_cost:
                    cost[ni][nj][idx] = next_running_cost
                    dfs((ni, nj), board,  distance + 1, corner_cnt + 1, idx)
                else:
                    return

def solution(board):
    global N, cost, answer
    answer = max_int
    N = len(board)
    cost = [[[max_int for _ in range(4)] for _ in range(N)] for _ in range(N)]
    for i in range(4):
        cost[0][0][i] = 0
        
    dfs((0, 0), board, 0, 0, -1)
    return answer

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
    
    