import sys
sys.stdin = open("보호필름.txt", "r")

import copy

def comb(lst,n):
    if n==0:
        return [[]]
    l=[]
    for i in range(0,len(lst)):
        m=lst[i]
        remLst=lst[i+1:]
        for p in comb(remLst,n-1):
            l.append([m]+p)
    return l

def perm(lst,n):
    if n==0:
        return [[]]
    l=[]
    for i in range(0,len(lst)):
        m=lst[i]
        remLst=lst
        for p in perm(remLst,n-1):
            l.append([m]+p)
    return l

def check_depth(board, K, D, w_idx):
    result = False
    cnt = 0
    target_idx = board[0][w_idx]
    for i in range(D):
        idx = board[i][w_idx]

        if target_idx == idx:
            cnt += 1
        else:
            if cnt >= K:
                result = True
                return  result
            target_idx = idx
            cnt = 1

    if cnt >= K:
        result = True

    return result

def check_ok(board, K, D, W):
    result = True
    for j in range(W):
        result = check_depth(board, K, D, j)
        if not result:
            return result

    return result


def drop_chem(board, W, loc_cand, chem_cand):
    chem_board = [layer[:] for layer in board] # deepcopy 고친것
    for idx, depth in enumerate(loc_cand):
        for w in range(W):
            chem_board[depth][w] = chem_cand[idx]
    return chem_board

def solve():
    D, W, K = map(int, input().split())
    board = []
    for i in range(D):
        board.append(list(map(int, input().split())))
    # T = 0 check
    res = check_ok(board, K, D, W)
    if res:
        return 0

    for i in range(D): #
        solve_cnt = i + 1
        loc_candidates = comb(list(range(D)), solve_cnt) # 조합(N C k)
        chem_candidates = perm([0, 1], solve_cnt)# 중복 순열
        for loc_cand in loc_candidates: # 어디를 약을 뿌릴지
            for chem_cand in chem_candidates:# 어떤약을 뿌릴지
                chem_board = drop_chem(board, W, loc_cand, chem_cand)
                res = check_ok(chem_board, K, D, W)
                if res:
                    return solve_cnt


if __name__ =="__main__":
    T = int(input())
    # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
    for test_case in range(1, T + 1):
        ans = solve()
        print(f"#{test_case} {ans}")