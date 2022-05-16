dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

def check_board_clear(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                return False
    
    return True


def DFS(board, card_history, cur_r, cur_c, num_moves):
    global MIN_MOVES
    
    print(card_history)
    for b in board:
        print(b)
    print("-------------")
        
        
    if check_board_clear(board):
        if num_moves<MIN_MOVES:
            MIN_MOVES = num_moves 
        return
    
    # CLICK ENTER 반영후 원상복귀
    if board[cur_r][cur_c] !=0:
        card = board[cur_r][cur_c]
        if not (cur_r, cur_c) in card_history[card]:
            #flip
            card_history[card].append((cur_r, cur_c))
            
            if len(card_history)==2: # 2개 뒤집힌 겨우
                for (x, y) in card_history[card]:
                    board[x][y] = 0
                
                DFS(board, card_history, cur_r, cur_c, num_moves + 1)
                for (x, y)  in card_history[card]:
                    board[x][y] = card
            else: # 1개 뒤집힌 경우
                DFS(board, card_history, cur_r, cur_c, num_moves + 1)
                    
            card_history[card].pop()           

    # 그냥 움직인경우:
    for i in range(4):
        next_r = cur_r + dr[i]
        next_c = cur_c + dc[i]
        if 0<=next_r<4 and 0<= next_c<4:
            DFS(board, card_history, next_r, next_c, num_moves + 1)
        
    # CTRL MOVE
    for i in range(4):
        next_r = cur_r  + dr[i]
        next_c = cur_c  + dc[i]
        
        
        while 0<=next_r<4 and 0<= next_c<4 and board[next_r][next_c]==0:
            next_r = cur_r + dr[i]
            next_c = cur_c + dc[i]
        
        if 0<=next_r<4 and 0<= next_c<4:
            DFS(board, card_history, next_r, next_c, num_moves + 1)

        



def solution(board, r, c):
    answer = 0
    card_history = dict()
    
    for i in range(1, 6):
        card_history[i] = []
    
    DFS(board, card_history, r, c, 0)
    
    return MIN_MOVES


if __name__ == "__main__":
    print(solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]], 1, 0))
    # print(solution([[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]], 0, 1))
