# B ->A
# 우선순위 1개
# 먼저 방문하는 방이 같을순 없음
#
#
# tree 구조다 0 이 root 이다
# 선수 순회다.

# brute force? 아니겠지

edge_dict = None
before = None
after = None
visited = None


def callstack_dfs(start):
    global after
    stack = [start]
    visited[start] = True

    while stack:
        node = stack.pop()

        if before[node] != -1 and not visited[before[node]]:
            after[before[node]] = node  # a 다음에 b 를 방문해야한다.
            continue

        if after[node] != -1 and not visited[after[node]]:  # 우선 방문
            visited[after[node]] = True
            stack.append(after[node])
            continue

        for neigh in edge_dict[node]:
            if not visited[neigh]:
                visited[neigh] = True
                stack.append(neigh)


def solution(n, path, order):
    global edge_dict, visited, before, after
    visited = [False for _ in range(n)]
    edge_dict = [[] for _ in range(n)]
    before = [-1 for _ in range(n)]
    after = [-1 for _ in range(n)]

    for (a, b) in path:
        edge_dict[a].append(b)
        edge_dict[b].append(a)

    for (a, b) in order:
        before[b] = a  # b전에 a 를 방문해야한다.

    callstack_dfs(0)

    answer = 1
    for i in range(n):
        answer *= int(visited[i])

    return bool(answer)

print(solution(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[8,5],[6,7],[4,1]]))
print(solution(9, [[8,1],[0,1],[1,2],[0,7],[4,7],[0,3],[7,5],[3,6]], [[4,1],[5,2]]))
print(solution(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[4,1],[8,7],[6,5]]))