def solution(n, s, a, b, fares):
    cost_s2e = [[float("inf")]*(n+1) for _ in range(n+1)]
    # s node 에서 e node까지 가는 최소비용

    for fare in fares:
        x, y, cost = fare
        cost_s2e[x][y] = cost
        cost_s2e[y][x] = cost
        cost_s2e[x][x] = 0
        cost_s2e[y][y] = 0


    for i in range(1, n+1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                cost_s2e[i][j] = min(cost_s2e[i][j], cost_s2e[i][k] + cost_s2e[k][j])

    # for row in cost_s2e:
    #     print(row)
    # s i a
    # s i b
    answer = float("inf")
    for i in range(1, n+1):
        answer = min(answer, cost_s2e[s][i] + cost_s2e[i][a] + cost_s2e[i][b])

    return answer

print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))