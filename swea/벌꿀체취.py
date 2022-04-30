import sys
sys.stdin = open("벌꿀체취.txt", "r")

N = None
M = None
C = None

def nHc(seq, c):
    if c==0:
        return [[]]
    results = []
    for i in range(len(seq)):
        cur = seq[i]
        res = seq[i:] # 나를 포함하여
        for subres in nHc(res, c-1):
            results.append([cur] + subres)
    return results

def product(seq, c):
    if c==0:
        return [[]]
    results = []
    for i in range(len(seq)):
        cur = seq[i]
        res = seq # 나를 포함하여
        for subres in nHc(res, c-1):
            results.append([cur] + subres)
    return results

def nCc(seq, c):
    if c == 0:
        return [[]]

    results = []
    for i in range(len(seq)):
        cur = seq[i]
        res = seq[i+1:]  # 나를 포함 안함
        for subres in nCc(res, c - 1):
            results.append([cur] + subres)
    return results

def take_honey(si, sj, board):
    # C 보다 작고
    # 많이 뽑을 수록 이득
    honey_sum_max = 0
    for m in range(M, 0, -1): # M -> 1 개의 꿀에 대해
        m_candidates = nCc(list(range(M)), m)
        for m_candiate in m_candidates:
            tmp_sum = 0
            tmp_score = 0
            for dj in m_candiate:
                tmp_score += board[si][sj+dj]*board[si][sj+dj]
                tmp_sum += board[si][sj+dj]

            if tmp_score > honey_sum_max and tmp_sum<=C:
                honey_sum_max = tmp_score

    return  honey_sum_max

def solve(test_case):
    '''
    한케이스당 2,400,000 이하 필요
    NxN 벌통
    각 벌통에 꿀의양
    벌꿀을 채취하여 최대한 많은 수익

    2명 M개의 가로로 연속된 벌꿀 체취 j 방향
    겹치면 안됨.

    중복조합을 통해 row i, k pair 뽑기 n H 2
    조합을 통해 col j, l pair 뽑기 N-M+1 C 2

    (i,j), (k,l) 에 대하여 겹치지지 않는지 체크
    i==k and j + M > l 이면 충돌

    각 일꾼 C의 양 최대 수확    <=C
    수익은 각 벌통의 제곱
    '''
    global  N, M, C
    # get input
    N, M, C = map(int, input().split())

    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))

    # get row pair
    row_pairs = nHc(list(range(N)), 2)
    col_pairs = product(list(range(N - M + 1)), 2) # 0 ~ N-M 까지

    max_honey_total = 0

    for (i, k) in row_pairs:
        for (j, l) in col_pairs:
            if i==k and j<=l<j+M  : # 충돌
                continue
            if i==k and l<=j<l+M  : # 충돌
                continue
            # a (i,j) b(k,l) 최대 벌꿀 수확
            # sum 안 경계가 타이트하면 제곱의 합이 꿀의 갯수가 적어도 역적 될수있다.
            # 2 2 5 2^2 + 2^2 < 5^2
            a_honey = take_honey(i, j, board)
            b_honey = take_honey(k, l, board)

            tmp_total = a_honey + b_honey
            if tmp_total > max_honey_total:
                max_honey_total = tmp_total

    return max_honey_total

if __name__ == "__main__":
    T = int(input())
    for test_case in range(1, T+1):
        ans = solve(test_case)
        print(f"#{test_case} {ans}")
