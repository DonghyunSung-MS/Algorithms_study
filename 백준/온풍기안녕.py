from collections import  deque
R = None
C = None
K = None
W = None
board = None
wall_bool = None
temp_board = None

di = [None, 0, 0, -1, 1]
dj = [None, 1, -1, 0, 0]

def wind_blow(si, sj, aircon_type):
    global temp_board
    aircon_type_moves = dict()
    aircon_type_moves[1] = [[3,1], [1], [4, 1]]
    aircon_type_moves[2] = [[3,2], [2], [4, 2]]
    aircon_type_moves[3] = [[1,3], [3], [2, 3]]
    aircon_type_moves[4] = [[1,4], [4], [2, 4]]

    idx = aircon_type_moves[aircon_type][1][0]
    si = si + di[idx]
    sj = sj + dj[idx]

    #(si, sj, 5) 온풍기가 있는 칸과 바람이 나오는 방향에 있는 칸 사이에는 벽이 없다.
    visitied = [[False]*C for _ in range(R)]

    que = deque()
    que.append((si,sj,5))
    visitied[si][sj] = True
    while que:
        ci, cj, temp = que.popleft()

        temp_board[ci][cj] += temp

        for move in aircon_type_moves[aircon_type]:
            canwarm = True
            ni = ci
            nj = cj

            for idx in move:
                nbi = ni
                nbj = nj
                ni += di[idx]
                nj += dj[idx]
                if 0<=ni<R and 0<=nj<C and wall_bool[ni][nj][nbi][nbj]==0:
                    # not wall and witin bound
                    continue
                else:
                    canwarm = False

            if canwarm and temp>1 and not visitied[ni][nj]:
                visitied[ni][nj] = True
                que.append((ni, nj, temp-1))

def control_temp():
    global temp_board
    old_temp_board = temp_board
    new_temp_board = [l[:] for l in temp_board]

    for i in range(R):
        for j in range(C):
            if old_temp_board[i][j]>0:
                for idx in range(1, 5):
                    ni = i + di[idx]
                    nj = j + dj[idx]
                    if 0<=ni<R and 0<=nj<C and old_temp_board[i][j]>old_temp_board[ni][nj] \
                            and wall_bool[i][j][ni][nj]==0:
                        diff = old_temp_board[i][j]-old_temp_board[ni][nj]
                        diff = int(abs(diff)/4)
                        new_temp_board[i][j] -= diff
                        new_temp_board[ni][nj] += diff

    temp_board = new_temp_board

def dropedge():
    global temp_board
    for i in range(R):
        if temp_board[i][0]>0:
            temp_board[i][0]-=1
        if temp_board[i][C-1] > 0:
            temp_board[i][C-1] -= 1

    for j in range(1, C-1):
        if temp_board[0][j]>0:
            temp_board[0][j]-=1
        if temp_board[R-1][j] > 0:
            temp_board[R-1][j] -= 1

def print_M(M):
    for m in M:
        print(m)
    print("------------")


def solve():
    ### 입력
    global R,C,K,W, board, wall_bool, temp_board
    R, C, K = map(int, input().split())
    board = []
    for _ in range(R):
        board.append(list(map(int, input().split())))

    temp_board = [[0]*C for _ in range(R)]

    W = int(input())
    wall_bool = [[[[0 for _ in range(C)] for _ in range(R)] for _ in range(C)] for _ in range(R)]

    for _ in range(W):
        x, y, t = map(int, input().split())
        # start from 0
        x -= 1
        y -= 1
        if t==0:
            wall_bool[x][y][x-1][y] = 1
            wall_bool[x-1][y][x][y] = 1
        else:
            wall_bool[x][y][x][y+1] = 1
            wall_bool[x][y+1][x][y] = 1


    for trial in range(1, 101):
        # warm wind blow
        for i in range(R):
            for j in range(C):
                if 0<board[i][j]<=4:
                    wind_blow(i, j, board[i][j])

        # control temp
        control_temp()
        dropedge()

        # inspect
        flag = True
        for i in range(R):
            for j in range(C):
                if board[i][j]==5:
                    if temp_board[i][j]<K:
                        flag = False

        if flag:
            print(trial)
            return

    print(101)

solve()