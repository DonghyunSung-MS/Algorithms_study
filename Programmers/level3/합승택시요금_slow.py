# d(a) = d(b) + c(a,b)
# s - A 최소
# s - B 최소
# 겹치는 경로 빼기?
# ab 같이 따로
from collections import  deque

edges = None
costs = dict()
dp_cost = None  # (a,b)->cost

# A 4 1 5 6
# B 4 1 5 3 2


def BFS(sa, sb, fa, fb):
    global dp_cost

    dp_cost[sa][sb] = 0  # init
    que = deque()
    que.append((sa,sb))

    while que:
        ca, cb = que.popleft()

        for na in edges[ca]:
            for nb in edges[cb]:
                if ca==fa:
                    na = ca
                if cb == fb:
                    nb = cb

                if ca==cb and na==nb:
                    cost = costs[(ca, na)]
                else:
                    cost = costs[(ca, na)] + costs[(cb, nb)]
                if dp_cost[na][nb]==-1 or  dp_cost[na][nb] >  dp_cost[ca][cb] + cost:
                    dp_cost[na][nb] = dp_cost[ca][cb] + cost
                    que.append((na,nb))


def solution(n, s, a, b, fares):
    global edges, costs, dp_cost
    s = s - 1
    a = a-1
    b = b-1

    edges = [[] for _ in range(n)]
    dp_cost = [[-1 for _ in range(n)] for _ in range(n)]

    for fare in fares:
        e1, e2, cost = fare
        e1 -= 1
        e2 -= 1

        costs[(e1, e2)] = cost
        costs[(e1, e1)] = 0
        costs[(e2, e2)] = 0

        costs[(e2, e1)] = cost

        edges[e1].append(e2)
        edges[e2].append(e1)

    visited = [[False for _ in range(n)] for _ in range(n)]

    BFS(s, s, a, b)
    answer = dp_cost[a][b]
    return answer

print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))