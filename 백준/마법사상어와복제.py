N = 4
di = [0, -1, -1, -1, 0, 1, 1, 1]
dj = [-1, -1, 0, 1, 1, 1, 0, -1]

shark_i = [-1, 0, 1, 0]
shark_j = [0, -1, 0, 1]

def matrix_print(M):
    for m in M:
        print(m)
    print("===============")

def move_fish(fish_map, fish_smell, si, sj):
    def search(x, y, dir):
        for i in range(8):
            ndir = (dir - i)%8
            nx = x + di[ndir]
            ny = y + dj[ndir]
            if 0<=nx<N and 0<=ny<N and not(nx==si and ny==sj) and fish_smell[nx][ny]==0:
                return nx, ny, ndir

        return x, y, dir
    fish_map_new = [[[] for _ in range(N)] for _ in range(4)] # [x,y] = dirs

    for cx in range(N):
        for cy in range(N):
            for cdir in fish_map[cx][cy]:
                nx, ny, ndir = search(cx, cy, cdir)
                fish_map_new[nx][ny].append(ndir)

    return fish_map_new

def shark_moves(si, sj, fish_smell, fish_map):
    # 우 하 좌 상 순으로 우선순위

    def product(seq, c):
        if c==0:
            return [[]]
        results = []

        for i in range(len(seq)):
            m = seq[i]
            rest = seq
            for p in product(rest, c-1):
                results.append([m]+p)
        return  results

    cand_moves = product([3,2,1,0], 3)
    shark_results = []
    for moves in cand_moves:
        isok = True
        nsi = si
        nsj = sj
        fish_cnt = 0
        visted = [[False]*N for _ in range(N)]
        '''
        방문 처리 하실 때 처음 상어 위치 방문 처리 하고 시작하면 안됩니다
        테케 3회째에 상어 시작 위치에 물고기가 겹쳐있어서, 위로 올라갔다가 다시 내려와야 하는데 그걸 카운트를 못하네요
        '''
        for idx in moves:
            nsi += shark_i[idx]
            nsj += shark_j[idx]
            if 0<=nsi<N and 0<=nsj<N:
                if not visted[nsi][nsj]:
                    visted[nsi][nsj] = True
                    tmp_fish = len(fish_map[nsi][nsj])
                    fish_cnt += tmp_fish
            else:
                isok = False
        if isok:
            shark_results.append((fish_cnt, moves))

    shark_results.sort(reverse=True, key=lambda x: (x[0], -(x[1][0]*100 + x[1][1]*10 + x[1][2] + 111)))
    _, selected_move = shark_results[0]
    nsi = si
    nsj = sj

    for idx in selected_move:
        nsi += shark_i[idx]
        nsj += shark_j[idx]
        tmp_fish = len(fish_map[nsi][nsj])
        if tmp_fish > 0:
            fish_map[nsi][nsj] = []
            fish_smell[nsi][nsj] = 3

    return nsi, nsj

def solve():
    M, S = map(int, input().split())

    fish_map = [[[] for _ in range(N)] for _ in range(4)] # [x,y] = dirs
    for _ in range(M):
        x, y, dir = map(int, input().split())
        fish_map[x-1][y-1].append(dir-1)

    si, sj = map(int, input().split())
    si -= 1
    sj -= 1
    fish_smell = [[0]*N for _ in range(N)]

    ###############################################
    for time in range(S):
        fish_map_copy = [[x[:] for x in l] for l in fish_map]
        fish_map = move_fish(fish_map, fish_smell, si, sj)
        si, sj = shark_moves(si, sj, fish_smell, fish_map)
        for i in range(N):
            for j in range(N):
                if fish_smell[i][j] > 0:
                    fish_smell[i][j] -= 1

        for i in range(N):
            for j in range(N):
                if len(fish_map_copy[i][j]) > 0:
                    fish_map[i][j].extend(fish_map_copy[i][j])

    ans = 0
    for i in range(N):
        for j in range(N):
            ans += len(fish_map[i][j])

    print(ans)
if __name__ == "__main__":
    solve()