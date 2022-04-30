# 4<=N<=100

N, K = map(int, input().split())

board = [[0]*N for _ in range(N)]

tmp = list(map(int, input().split()))
for i in range(N):
    board[0][i] = tmp[i]

di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]

def print_NxN():
    for i in range(N):
        print(board[i][:N])

def find_min_and_add_fish():
    min_fish = float("inf")
    for i in range(N):
        if board[0][i] < min_fish:
            min_fish = board[0][i]
    for i in range(N):
        if board[0][i] == min_fish:
            board[0][i] += 1

def flip_until():
    p = 0
    w = 1
    h = 1
    for idx in range(N):
        if p+w+h>N:
            break

        for j in range(p, p+w):
            for i in range(h):
                tmp = board[i][j]
                board[w - j + p][p+i+w] = tmp
                board[i][j] = 0
        p += w
        if idx%2==0:
            h+=1
        else:
            w+=1

def sortfish():
    global  board
    tmpboard = [l[:] for l in board]
    for ci in range(N):
        for cj in range(N):
            if board[ci][cj] > 0: #fish
                for idx in range(4):
                    ni = ci + di[idx]
                    nj = cj + dj[idx]
                    if 0<=ni<N and 0<=nj<N and board[ni][nj]>0:
                        next_fish = board[ni][nj]
                        cur_fish = board[ci][cj]
                        diff = int((cur_fish - next_fish)/5)
                        if cur_fish > next_fish:
                            tmpboard[ni][nj] += diff
                            tmpboard[ci][cj] -= diff

    board = tmpboard

def make_line():
    tmp_list = []
    for j in range(N):
        for i in range(N):
            tmp = board[i][j]
            if tmp>0:
                tmp_list.append(tmp)
                board[i][j] = 0

    for j in range(N):
        board[0][j] = tmp_list[j]

def fold_2times():
    ind1 = int(N/2)
    ind2 = int(N/4)

    for j in range(ind1):
        tmp = board[0][j]
        board[1][N-1-j] = tmp
        board[0][j] = 0

    for j in range(N-ind1, N-ind2):
        for i in range(2):
            tmp = board[i][j]
            board[3 - i][2*N-j-ind1-1] = tmp
            board[i][j]=0


def min_max_diff():
    return max(board[0]) - min(board[0])

if __name__ == "__main__":
    cnt = 0
    diff = min_max_diff()

    while True:
        if diff<=K:
            break
        find_min_and_add_fish()
        flip_until()
        sortfish()
        make_line()
        fold_2times()
        sortfish()
        make_line()
        cnt += 1
        diff = min_max_diff()

    print(cnt)
