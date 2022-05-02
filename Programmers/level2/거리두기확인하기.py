'''
5x5 크기 대기실
맨해튼 거리 abs()+abs()<=2 안됨
맨해튼 거리 abs()+abs()>2 됨

파티션오키

'''
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def dfs(sx, sy, board):
    stack = [(sx, sy)]
    visited = [[False] * 5 for _ in range(5)]
    visited[sx][sy] = True
    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dist = abs(nx - sx) + abs(ny - sy)
            if 0 <= nx < 5 and 0 <= ny < 5 and board[nx][ny] != 1 and dist <= 2 and not visited[nx][ny]:
                visited[nx][ny] = True
                stack.append((nx, ny))
                # 칸막이가 아니면 맨핸터리 <=2 아직 안방문
                if board[nx][ny] == -1: #사람이면
                    return False


    return True


def check_possible(board):
    for i in range(5):
        for j in range(5):
            if board[i][j] == -1:  # 사람
                res = dfs(i, j, board)
                if not res:
                    return 0
    return 1


def solution(places):
    answer = []

    for place in places:
        # place to 5x5 board
        # 빈공간 0 파티션 1 사람 -1
        board = [[0] * 5 for _ in range(5)]
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    board[i][j] = -1
                elif place[i][j] == "X":
                    board[i][j] = 1

        result = check_possible(board)
        answer.append(result)

    return answer