MOVES = [[1, 0], [0, 1], [-1, 0], [0, -1]]
M = None
N = None

def within(loc):
    global M, N
    if loc[0]>=0 and loc[1]>=0 and loc[0]<M and loc[1]<N:
        return True
    else:
        return False
    
def one_trial(board, aloc, bloc, turn, num_move):
    global MOVES
    # turn 0 a move
    # turn 1 b move
    # 종료 조건 내가 못 움직이거나
    # 내 위치가 0 이되거나
    
    # 최선의 행동을 어떻게?
    #print(board, aloc, bloc, turn, a_move, b_move)
    
    if turn==0:
        a_returns = []
        cnt = 0
        if board[aloc[0]][aloc[1]] == 0:
            return (0, num_move)
        
        for move in MOVES:
            nxt = [aloc[0]+move[0], aloc[1]+move[1]]
            if within(nxt) and board[nxt[0]][nxt[1]] == 1:
                board[aloc[0]][aloc[1]] = 0
                a_return = one_trial(board, nxt, bloc, 1, num_move + 1)
                board[aloc[0]][aloc[1]] = 1
                a_returns.append(a_return)
            else:
                cnt +=1
        if cnt == 4:
            return (0, num_move)
        
        final_move
        for flag, move in a_returns:
            if flag==1: #A win
                
        
    elif turn==1:
        cnt = 0
        if board[bloc[0]][bloc[1]] == 0:
            return (1, num_move)
        
        for move in MOVES:
            nxt = [bloc[0]+move[0], bloc[1]+move[1]]
            if within(nxt) and board[nxt[0]][nxt[1]] == 1:
                board[bloc[0]][bloc[1]] = 0
                one_trial(board, aloc, nxt, 0, num_move + 1)
                board[bloc[0]][bloc[1]] = 1          
            else:
                cnt +=1
        if cnt == 4:
            return (1, num_move)
def solution(board, aloc, bloc):
    global M, N, RESULTS
    num_move = 0
    # M x N
    M = len(board)
    N = len(board[0])
    answer = one_trial(board, aloc, bloc, 0, 0, 0)
    print(RESULTS)
    
    
    return answer