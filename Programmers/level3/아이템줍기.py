from collections import deque
MAX = 120
board = [[0 for _ in range(MAX)] for _ in range(MAX)]


def edges_cand(rec):
    a, b, c, d = rec
    edges = set()
    # [a, c], b
    # [a, c], d
    
    for x in range(a, c+1):
        edges.add((x, b))
        edges.add((x, d))
    # a [b, d]
    # c [b, d]
    for y in range(b, d+1):
        edges.add((a, y))
        edges.add((c, y))
    return list(edges)
    
def within(edge, rectangle):
    x, y = edge
    for a, b, c, d in rectangle:
        if a<x<c and b<y<d:
            return True
        
    return  False

def bfs(sx, sy, ex, ey):
    visit = set()
    visit.add((sx, sy))
    
    que = deque()
    que.append((sx, sy, 0))
    
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    while que:
        cx, cy, move = que.popleft()
        if ex==cx and ey==cy:
            return move
        
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if (nx, ny) not in visit and board[ny][nx]==1:
                que.append((nx, ny, move + 1))
                visit.add((nx, ny))
            
        
def solution(rectangle, characterX, characterY, itemX, itemY):
    '''
    2 배로 늘려 모호함(코너인지 등) 제거.
    3중 loop로 최대한 외곽만을 그리기
        1칸(0.5) 이동에 대해서 겹치는 영역이 없도록

    bfs를 통한 최단경로 계산
    '''
    N = len(rectangle)
    for i in range(N):
        for j in range(4):
            rectangle[i][j]*=2
    
    
    for target_rec in rectangle:
        edges = edges_cand(target_rec)
        for edge in edges:
            x, y = edge
            if within(edge, rectangle):
                board[y][x] = 0
            else:
                board[y][x] = 1

    sx = characterX*2
    sy = characterY*2
    
    ex = itemX*2
    ey = itemY *2
    
    return bfs(sx, sy, ex, ey)//2