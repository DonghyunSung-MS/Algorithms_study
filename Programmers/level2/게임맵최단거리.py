from collections import deque

N = None
M = None
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def solution(maps):
    N = len(maps)
    M = len(maps[0])
    
    que = deque()
    que.append((0, 0, 1))
    vistied = [[False]*M for _ in range(N)]
    vistied[0][0] = True
    
    while que:
        cx, cy, dist = que.popleft()
        
        if cx==N-1 and cy==M-1:
            return dist
    
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0<=nx<N and 0<=ny<M and not vistied[nx][ny] and maps[nx][ny]==1:
                vistied[nx][ny]=True
                que.append((nx, ny, dist + 1))
            
    
    return -1