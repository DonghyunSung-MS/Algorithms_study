import sys
sys.stdin = open("벽돌깨기.txt", "r")

'''
16진수 (0~F)
'''
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
ans = None
W = None
H = None
N = None
def print_2dlist(B):
    for b in B:
        print(b)

def drop_gravity(board):
    new_board = [[0 for _ in range(W)] for _ in range(H)]

    for j in range(W):
        new_i = H - 1
        for i in range(H-1, -1, -1): # reverse order
            if board[i][j] !=0:
                new_board[new_i][j] = board[i][j]
                new_i -=1

    return  new_board


def chain_reaction(sj, board):
    si = 0
    for i in range(H):
        if board[i][sj]!=0:
            si = i
            break
    # si, sj 구슬 시작
    stack = [(si, sj)]
    cnt = 0
    while stack:
        ci, cj = stack.pop()
        n_bomb = board[ci][cj]
        if board[ci][cj] == 0:
            continue
        board[ci][cj] = 0# erase block
        cnt += 1
        for idx in range(4): # direction
            for length in range(n_bomb):
                ni = ci + di[idx] * length
                nj = cj + dj[idx] * length
                if 0<=ni<H and 0<=nj<W and board[ni][nj] !=0:
                    stack.append((ni, nj))

    return board, cnt

def dfs(num_trial, board, cnt):
    global ans
    if num_trial>=N: # 종료조건
        if cnt > ans:
            ans = cnt
        return

    for j in range(W):
        tboard = [l[:] for l in board] # create new instance    
        tboard, new_cnt = chain_reaction(j, tboard)
        tboard = drop_gravity(tboard)
        dfs(num_trial + 1, tboard, cnt + new_cnt)


def solve():
    global  ans, N, W, H
    ans = -float("inf")

    N, W, H = map(int, input().split())
    board = []
    for _ in range(H):
        board.append(list(map(int, input().split())))

    init_cnt = 0
    for i in range(H):
        for j in range(W):
            if board[i][j] !=0:
                init_cnt +=1

    dfs(0, board, 0)
    return init_cnt - ans

if __name__ == "__main__":
    T = int(input())
    for test_case in range(1,T+1):
        left = solve()
        print(f"#{test_case} {left}")
