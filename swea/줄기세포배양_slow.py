import sys
sys.stdin = open("줄기세포배양.txt", "r")
from collections import deque

#  비효율적인

N = None
M = None
K = None
di = [0, 0, 1, -1]
dj = [1, -1,0, 0]
def solve():
    global  N, M, K
    N, M, K = map(int, input().split())

    live_cell_board = []
    tmp_board = []
    for i in range(N):
        tmp_board.append(list(map(int, input().split())))

    for i in range(N):
        for j in range(M):
            if tmp_board[i][j]!=0:
                live_cell_board.append((i, j, tmp_board[i][j], tmp_board[i][j]+0, tmp_board[i][j]*2+0))
                #(a, b) t<a 비활, a<=t<b 활 t>=b 죽, t==a+1 번식

    # O(cell*K *)
    death_cell_board = []
    for t in range(1, K + 1): # 1~K
        reproduce_dict = {}

        live_cell_board_old = [l[:] for l in live_cell_board]
        live_cell_board = []
        for cell in live_cell_board_old:
            i, j, size, a, b = cell
            if t == a + 1: # 번식
                for idx in range(4):
                    ni = i + di[idx]
                    nj = j + dj[idx]
                    if (ni, nj) in reproduce_dict.keys(): #
                        if size > reproduce_dict[(ni, nj)]:
                            reproduce_dict[(ni, nj)] = size
                    else:
                        reproduce_dict[(ni, nj)] = size

            if t < b:
                live_cell_board.append((i, j, size, a, b))
            else:
                death_cell_board.append((i,j,size,a,b))


        if len(reproduce_dict.keys())>0:
            for (ri, rj), rsize in reproduce_dict.items():
                isin = False
                for cell in live_cell_board + death_cell_board:
                    i, j, size, a, b = cell
                    if ri==i and rj==j:
                        isin = True

                if not isin:
                    live_cell_board.append((ri, rj, rsize, rsize+t, rsize*2 + t))

    return len(live_cell_board)

if __name__ == "__main__":
    T = int(input())
    for test_case in range(1, T+1):

        ans = solve()
        print(f"#{test_case} {ans}")
        # break