import sys
sys.stdin = open("특이한자석.txt", "r")
from collections import  deque

di = [-1, 1]
def one_step(mangnets, idx, dir):
    # 회전하기 전에 N==S체크해서 반대 방향으로 돌리기
    stack = [(idx, dir)]
    candidates = [(idx, dir)]

    visited = [False] * 4
    visited[idx] = True
    while stack:
        idx, dir = stack.pop()
        for i in range(2):
            ndx = idx + di[i]
            if 0<=ndx<4 and not visited[ndx]:
                if ndx>idx:
                    if mangnets[idx][2] != mangnets[ndx][6]:
                        visited[ndx] = True
                        stack.append((ndx, -dir))
                        candidates.append((ndx, -dir))
                if ndx < idx:
                    if mangnets[idx][6] != mangnets[ndx][2]:
                        visited[ndx] = True
                        stack.append((ndx, -dir))
                        candidates.append((ndx, -dir))

    # change magnet
    for idx, dir in candidates:
        tmp = mangnets[idx]
        if dir == 1:
            tmp = [tmp[-1]] + tmp[0:-1]
        else:
            tmp = tmp[1:] + [tmp[0]]

        mangnets[idx] = tmp

    return  mangnets
def solve():
    '''
    magnets = [list(), list(), list(), list()]
    list[0]  빨간점 위치
    list[2]  오른쪽
    list[6]  왼쪽
    '''
    K = int(input())
    magnets = []
    for i in range(4):
        tmp = list(map(int, input().split()))
        magnets.append(tmp)

    actions = []
    for k in range(K):
        idx, dir = map(int, input().split())
        actions.append((idx - 1, dir))


    for k in range(K):
        idx, dir = actions[k]
        mangnets = one_step(magnets, idx, dir)

    sum = 0
    for i in range(4):
        if mangnets[i][0] == 1: # s극 이면
            sum += (2**i)

    return sum

if __name__ == "__main__":
    T = int(input())
    for test_case in range(1, T+1):
        ans = solve()
        print(f"#{test_case} {ans}")