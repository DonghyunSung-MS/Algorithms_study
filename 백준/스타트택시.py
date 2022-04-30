"""
손님 목적지 완료시 연료 자동충전
연료 바닥시 영업종료

M명 승객
NxN격자 최단경로 이동

현위치에서 가장 가까운 승객부터 태움(BFS low depth)

윗손님 부터 low i -> low j

승객태워 이동 완료 소모한 연료의 2배
"""
from collections import deque

N = None # N 그리드 0 빈칸 1 벽
M = None # M승객
F = None # 연료
BOARD = [] # 그리드
si, sj = 0, 0 # 택시 시작위치
P = [] # M x 4[si, sj, gi, gj]

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def zero_NxN():
    return [[0] * N for _ in range(N)]

def get_input():
    global N, M, F, BOARD, si, sj, P
    N, M, F = map(int, input().split())
    
    for _ in range(N):
        BOARD.append(list(map(int, input().split())))
    
    si, sj = map(int, input().split()) # 1~N -> 0 ~ N-1
    si, sj = si-1, sj -1 # 1~N -> 0 ~ N-1
    
    for _ in range(M):
        tmp = list(map(int, input().split()))
        for i in range(4):
            tmp[i] = tmp[i] -1
        
        P.append(tmp)
                

def bfs_passenger(start):
    i, j = start
    dist = 0
    visited = zero_NxN()
    q = deque([(i, j, dist)])
    min_dist = float("inf")
    
    results = []
    while q:
        cur_i, cur_j, cur_d = q.popleft()
        
        if visited[cur_i][cur_j] > min_dist:
            break
        
        for p_idx in range(M):
            if cur_i == P[p_idx][0] and cur_j == P[p_idx][1]:
                results.append((cur_i, cur_j, cur_d, p_idx))
                min_dist = visited[cur_i][cur_j]
                
        for idx in range(4):
            nex_i = cur_i + di[idx]
            nex_j = cur_j + dj[idx]
            nex_d = cur_d + 1
            # within boudary and not visitied not wall
            if 0<=nex_i<N and 0<=nex_j<N and visited[nex_i][nex_j]==0 and BOARD[nex_i][nex_j] == 0:
                visited[nex_i][nex_j] = visited[cur_i][cur_j] + 1
                q.append((nex_i, nex_j, nex_d))
                    
    return sorted(results, key=lambda x: (x[2], x[0], x[1]))
    
def bfs_goal(start, goal):
    i, j = start
    dist = 0
    visited = zero_NxN()
    q = deque([(i, j, dist)])
    visited[i][j]==1
    
    while q:
        cur_i, cur_j, cur_d = q.popleft()
        for idx in range(4):
            nex_i = cur_i + di[idx]
            nex_j = cur_j + dj[idx]
            nex_d = cur_d + 1
            # within boudary and not visitied not wall
            if 0<=nex_i<N and 0<=nex_j<N and visited[nex_i][nex_j]==0 and BOARD[nex_i][nex_j] == 0:
                visited[nex_i][nex_j] = 1
                q.append((nex_i, nex_j, nex_d))
                if nex_i == goal[0] and nex_j == goal[1]:
                    return nex_d                    

    return -1

if __name__ == "__main__":
    get_input()
    #사람 마다 태우러가고 태우러오고 열료 체크하고
    fish_code = True
    
    for _ in range(M):
        results = bfs_passenger((si, sj))
        if len(results) == 0:
            fish_code = False
            break
        
        si, sj, take_dist, p_idx = results[0]
        if F < take_dist:
            fish_code = False
            break
        else:
            F = F - take_dist
        goal_dist = bfs_goal((si, sj), P[p_idx][2:4])
        if goal_dist == -1:
            fish_code = False
            break
        
        if F < goal_dist:
            fish_code = False
            break
        else:
            F = F + goal_dist
            si, sj = P[p_idx][2:4]    

        # 다 된 손님에게 이상한 좌표주기
        P[p_idx] = [-1, -1, -1, -1]
        
    if fish_code:
        print(F)
    else:
        print(-1)