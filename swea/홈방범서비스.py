import sys
sys.stdin = open("홈방범서비스.txt", "r")

N = None
M = None


def count_house_within(ci, cj, K, board):
    cost = K * K + (K - 1) * (K - 1)
    house_cnt = 0
    for di in range(-(K-1), K):
        for dj in range(-(K-1), K):
            dist = abs(di) + abs(dj)
            ni = ci + di
            nj = cj + dj
            if 0<=ni<N and 0<=nj<N and dist<K and board[ni][nj]==1:
                house_cnt += 1

    profit = house_cnt * M - cost

    if profit >= 0: # 손해를 보지 않는다 양수이다.
        return house_cnt
    else:
        return 0


def solve():
    '''
    cost = k*k + (k-1)*(k-1)
    도시 벗어나도 비용 동일

    집하나 비용 M 지불

    K = 2, cost = 5, earn = M*num_house profit = earn - cost = 4

    최대 house with profit > 0
    K = 1 ->
    K = 2 ->
    K는 최대 N+1 이하

    범위 abs(cx - nx) + abs(cy-ny)<K

    '''
    global M,N
    N, M = map(int, input().split())
    board = []
    for i in range(N):
        board.append(list(map(int, input().split())))

    # O(N^2)에 대하여 K는 N+1까지 2K^2  = 20*20*21*20*20*2
    # 완전탐색으로 해도 1억이 안된다.
    ans = 0
    for i in range(N):
        for j in range(N):
            for k in range(1, N+2):
                cnt = count_house_within(i, j, k, board)
                if cnt > ans:
                    ans = cnt

    return ans

if __name__ == "__main__":
    T = int(input())
    for test_case in range(1, T+1):
        ans = solve()
        print(f"#{test_case} {ans}")