import sys
sys.stdin = open("줄기세포배양.txt", "r")
from collections import deque

#  효율적인 고치기

N = None
M = None
K = None
di = [0, 0, 1, -1]
dj = [1, -1,0, 0]

def solve():
    global  N, M, K
    N, M, K = map(int, input().split())

    cell_board = [[0]*(M+2*K) for _ in range(N+2*K)]
    tmp_board = []
    for i in range(N):
        tmp_board.append(list(map(int, input().split())))

    live_que = deque()

    for i in range(N):
        for j in range(M):
            size = tmp_board[i][j]
            if size>0:
                cell_board[i+K][j+K] = size
                live_que.append((i+K,j+K,size,size,size*2))
                #(x, y, size, a, b) t<a 비활, a<=t<b 활 t>=b 죽, t==a+1 번식

    death_que = deque()

    for t in range(1, K + 1): # 1~K
        next_live_que = deque()
        reproduce_dict = {}

        while live_que:
            i, j, size, a, b = live_que.pop()
            if t == a + 1:  # 번식
                for idx in range(4):
                    ni = i + di[idx]
                    nj = j + dj[idx]
                    if (ni, nj) in reproduce_dict.keys(): #
                        if size > reproduce_dict[(ni, nj)]:
                            reproduce_dict[(ni, nj)] = size
                    else:
                        reproduce_dict[(ni, nj)] = size

            if t < b:
                next_live_que.append((i, j, size, a, b))
            else:
                death_que.append((i,j,size,a,b))

        if len(reproduce_dict.keys())>0:
            for (ri, rj), rsize in reproduce_dict.items():
                if cell_board[ri][rj]==0:
                    cell_board[ri][rj] = rsize
                    next_live_que.append((ri, rj, rsize, rsize+t, rsize*2 + t))

        live_que = next_live_que


    return len(live_que)




if __name__ == "__main__":
    T = int(input())
    for test_case in range(1, T+1):

        ans = solve()
        print(f"#{test_case} {ans}")
