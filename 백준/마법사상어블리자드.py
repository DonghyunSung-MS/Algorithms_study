from collections import deque

di = [None, -1, 1, 0, 0]
dj = [None, 0, 0, -1, 1]

board = None
N = None
M = None
idx2ij_dict = None
idx_map = None
broken_ball_cnts = [0, 0, 0, 0]


def print_M(M):
    for m in M:
        print(m)
    print("----")

def make_idx2ij():
    global idx2ij_dict, idx_map
    idx2ij_dict = dict()
    idx_map = [[0]*N for _ in range(N)]

    dir_idx_order = [4, 2, 3, 1]
    i = 0
    j = 0
    dir_idx = 0

    visited = [[False]*N for _ in range(N)]


    for start in range(N*N - 1, -1, -1):
        idx2ij_dict[start] = (i, j)
        idx_map[i][j] = start

        visited[i][j] = True
        ni = i + di[dir_idx_order[dir_idx]]
        nj = j + dj[dir_idx_order[dir_idx]]

        if 0<=ni<N and 0<=nj<N and not visited[ni][nj]:
            i = ni
            j = nj
        else:
            ni -= di[dir_idx_order[dir_idx]]
            nj -= dj[dir_idx_order[dir_idx]]

            dir_idx = (dir_idx + 1)%4
            i += di[dir_idx_order[dir_idx]]
            j += dj[dir_idx_order[dir_idx]]

def solve():
    global N, M, board
    N, M = map(int, input().split())
    board = []
    magics = [] #(d,s)
    for _ in range(N):
        board.append(list(map(int, input().split())))
    for _ in range(M):
        magics.append(list(map(int, input().split())))

    make_idx2ij()

    for (d,s) in magics:
        break_ball_magic(d, s)

        fill_between()
        result = True
        while result:
            result = break_ball_sequence_once()
            fill_between()
        transform_ball()

    ans = broken_ball_cnts[1] + broken_ball_cnts[2]*2 + broken_ball_cnts[3]*3
    print(ans)

def transform_ball():
    '''
    1,1->2,1
    2 -> 1,2
    '''
    # find sequence and make 0
    idx1 = 1
    idx2 = 1
    i, j = idx2ij_dict[idx1]
    cur_ball = board[i][j]


    que = deque()

    while idx1 < N * N and idx2 < N * N:
        if cur_ball == 0:  # 구슬이없으면
            break
        cnt = 0
        while True:
            i, j = idx2ij_dict[idx2]
            next_ball = board[i][j]
            if next_ball == cur_ball:
                cnt += 1
            else:
                break
            idx2 += 1

        # 구슬 변화
        que.append(cnt) #A
        que.append(cur_ball) #B

        idx1 = idx2
        idx2 = idx1
        i, j = idx2ij_dict[idx1]
        cur_ball = board[i][j]

    idx = 1
    while que and idx<N*N:
        ball_name = que.popleft()
        i, j = idx2ij_dict[idx]
        board[i][j] = ball_name

        idx += 1

def break_ball_sequence_once():
    # find sequence and make 0
    idx1 = 1
    idx2 = 1
    i, j = idx2ij_dict[idx1]
    cur_ball = board[i][j]

    isbreak = False
    while idx1<N*N and idx2 < N*N:
        if cur_ball==0:#구슬이없으면
            break
        cnt = 0
        tmp_list = [(i, j)]
        while True:
            i, j = idx2ij_dict[idx2]
            tmp_list.append((i, j))
            next_ball = board[i][j]
            if next_ball == cur_ball:
                cnt +=1
            else:
                tmp_list.pop()
                break
            idx2 +=1

        # 구슬 붕괴
        if cnt >=4:
            isbreak = True
            for (i, j) in tmp_list:
                tmp_ball = board[i][j]
                broken_ball_cnts[tmp_ball] += 1
                board[i][j] = 0

        idx1 = idx2
        idx2 = idx1
        i, j = idx2ij_dict[idx1]
        cur_ball = board[i][j]

    return isbreak

def fill_between():

    que = deque()
    for idx in range(N*N):
        i, j = idx2ij_dict[idx]
        if board[i][j]>0:
            que.append(board[i][j])
            board[i][j] = 0
    idx = 1 # 상어 아닌곳부터 시작
    while que and idx<N*N:
        ball_name = que.popleft()
        i, j = idx2ij_dict[idx]
        board[i][j] = ball_name

        idx += 1

def break_ball_magic(d, s):
    global broken_ball_cnts
    center_i, center_j = int((N-1)/2), int((N-1)/2)
    for scale in range(1, s+1):
        cur_ball_num = board[center_i+di[d]*scale][center_j+dj[d]*scale]
        if cur_ball_num>0:
            board[center_i+di[d]*scale][center_j+dj[d]*scale] = 0
            # broken_ball_cnts[cur_ball_num] +=1

if __name__ == "__main__":
    solve()