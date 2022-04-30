import sys
sys.stdin = open("핀볼게임.txt", "r")

# 로직 구현
# 블록 0~5
block_dir_map = {
    0:{0:0,1:1,2:2,3:3},
    1:{0:2,1:3,2:1,3:0},
    2:{0:2,1:0,2:3,3:1},
    3:{0:3,1:2,2:0,3:1},
    4:{0:1,1:3,2:0,3:2},
    5: {0: 2, 1: 3, 2: 0, 3: 1},
}

warm_hole = {
    6:[],
    7:[],
    8:[],
    9:[],
    10:[],
}  # tuple -> tuple
direction = [(0, 1), (-1, 0), (0, -1), (1, 0)]

def simulation(si, sj, dir_idx, board, N):
    score = 0
    ci = si
    cj = sj
    while True:
        # move
        di, dj = direction[dir_idx]
        ci += di
        cj += dj
        #check wall
        if ci<0 or ci>=N or cj<0 or cj>=N:
            # 벽 방향 바꾸고
            # same as block 5
            dir_idx = block_dir_map[5][dir_idx]
            score += 1
            continue

        cur_block_type = board[ci][cj]
        # check type
        if 1<=cur_block_type<=5: # block
            dir_idx = block_dir_map[cur_block_type][dir_idx]
            score += 1
        elif 6 <= cur_block_type <= 10:  # 웜홀
            warm_hole_idx = -1
            for idx, (w_i, w_j) in enumerate(warm_hole[cur_block_type]):
                if ci==w_i and cj==w_j:
                    warm_hole_idx = idx
            ci, cj = warm_hole[cur_block_type][(warm_hole_idx + 1)%2] # 여기 실수 코드

        if (ci==si and cj==sj) or board[ci][cj]==-1:
            return score



def solve():
    global warm_hole
    ################# get input
    N = int(input())
    board = []
    # 웜홀
    for _ in range(N):
        board.append(list(map(int, input().split())))

    for i in range(N):
        for j in range(N):
            block_type = board[i][j]
            if 6<=block_type<=10:
                warm_hole[block_type] += [[i, j]]

    max_score = -float("inf")
    ########################### brute force simulation
    # print(simulation(2, 3, 0, board, N))
    # return
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                for k in range(4):
                    score = simulation(i, j, k, board, N)
                    if score > max_score:
                        max_score = score

    warm_hole = {
        6: [],
        7: [],
        8: [],
        9: [],
        10: [],
    }  # tuple -> tuple
    return max_score

if __name__=="__main__":
    T = int(input())
    # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
    for test_case in range(1, T + 1):
        ans = solve()
        print(f"#{test_case} {ans}")
