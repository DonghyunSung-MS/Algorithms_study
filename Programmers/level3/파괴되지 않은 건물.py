N = None
M = None

def change(diff, r1, c1, r2, c2, degree):
    diff[r1][c1] += degree
    diff[r2+1][c1] += -degree
    diff[r1][c2+1] += -degree
    diff[r2+1][c2+1] += degree

def diff_reconst(diff):
    for i in range(N):
        for j in range(M):
            diff[i][j+1]+=diff[i][j]
            
    for j in range(M):
        for i in range(N):
            diff[i+1][j]+=diff[i][j]

def printM(board):
    for b in board:
        print(b)
    print("------")

def solution(board, skill):
    global N, M
    N = len(board)
    M = len(board[0])
    diff = [[0]*(M+1) for _ in range(N+1)]
    
    # K    
    for typ, r1, c1, r2, c2, degree in skill:
        if typ==1: #하향
            change(diff, r1, c1, r2, c2, -degree)
        else: #회복
            change(diff, r1, c1, r2, c2, degree)
    diff_reconst(diff)
    
    cnt = 0
    for i in range(N):
        for j in range(M):
            board[i][j] += diff[i][j]
            if board[i][j]>0:
                cnt += 1
            
    return cnt