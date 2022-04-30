import sys
sys.stdin = open("요리사.txt", "r")

min_diff = None
board = None
N = None

def nPc(lst, c):
    if c==0:
        return [[]]

    result = []
    for i, ele in enumerate(lst):
        m = ele
        rest = lst[:i] + lst[i+1:]
        # rest = lst[i+1:] #조합
        for ele_prev in nPc(rest, c - 1):
            result.append([m]+ele_prev)

    return result

def dfs(depth, a_list, b_list):
    global min_diff

    if depth >= N:
        # calculate score
        # 순서의미 있음 [0, 1] 요리 [1,0] 요리 값 다름
        # nP2 [(0,1),(1,2),...]
        a_sum = 0
        for (i, j) in nPc(a_list, 2):
            a_sum += board[i][j]

        b_sum = 0
        for (i, j) in nPc(b_list, 2):
            b_sum += board[i][j]

        result = abs(a_sum - b_sum)

        if result < min_diff:
            min_diff = result

        return

    if len(a_list) < N//2:
        dfs(depth+1, a_list+[depth], b_list)

    if len(b_list) < N // 2:
        dfs(depth + 1, a_list, b_list+[depth])


def solve():
    global  min_diff, N, board
    min_diff = float("inf")
    N = int(input())
    board = []
    for i in range(N):
        board.append(list(map(int, input().split())))

    dfs(0, [], [])


    return min_diff

if __name__ == "__main__":
    T = int(input())
    for test_case in range(1, T+1):
        ans = solve()
        print(f"#{test_case} {ans}")
