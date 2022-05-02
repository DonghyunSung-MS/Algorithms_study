dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
N = None
M = None


def dfs(si, sj, sdir, visited, grid):
    stack = [(si, sj, sdir)]
    visited[si][sj][sdir] = True

    cycle_len = 0
    while stack:
        ci, cj, cdir = stack.pop()

        ni = (ci + dx[cdir]) % N
        nj = (cj + dy[cdir]) % M
        ndir = None
        if grid[ni][nj] == "S":
            ndir = cdir
        elif grid[ni][nj] == "R":
            ndir = (cdir + 1) % 4
        elif grid[ni][nj] == "L":
            ndir = (cdir - 1) % 4

        cycle_len += 1

        if ni == si and nj == sj and sdir == ndir:
            return cycle_len
        else:
            visited[ni][nj][ndir] = True
            stack.append((ni, nj, ndir))


def solution(grid):
    global N, M
    answer = []
    # Nx M
    N = len(grid)
    M = len(grid[0])

    # NxMx4
    visited = [[[False for _ in range(4)] for _ in range(M)] for _ in range(N)]


    for i in range(N):
        for j in range(M):
            for dir in range(4):
                if not visited[i][j][dir]:
                    length = dfs(i, j, dir, visited, grid)
                    answer.append(length)

    return sorted(answer)

if __name__=="__main__":
    """
    ["SL","LR"]	[16]
    ["S"]	[1,1,1,1]
    ["R","R"] [4,4]
    """
    print(solution(["SSS"]))
    print(solution(["S"]))
    print(solution(["R","R"]))