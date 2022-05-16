from collections import deque
from itertools import permutations

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

def check_board_clear(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                return False
    
    return True

def check_wall(r, c, dir_idx):
    if dir_idx == 0:
        return c==0
    elif dir_idx ==1:
        return c==3
    elif dir_idx==2:
        return r==0
    elif dir_idx==3:
        return r==3

def new2d(M):
    return [m[:] for m in M]


def getmindist(board, from_r, from_c, to_r, to_c):
    
    dp_dists = [[float("inf")]*4 for _ in range(4)]
    
    stack = [(from_r, from_c)]
    dp_dists[from_r][from_c] = 0
    
    while stack:
        cur_r, cur_c = stack.pop()      
        
        # 그냥 움직인경우:
        for i in range(4):
            next_r = cur_r + dr[i]
            next_c = cur_c + dc[i]
            if 0<=next_r<4 and 0<= next_c<4:
                if dp_dists[next_r][next_c] > dp_dists[cur_r][cur_c] + 1:
                    dp_dists[next_r][next_c] = dp_dists[cur_r][cur_c] + 1
                    stack.append((next_r, next_c))
            
        # CTRL MOVE
        for i in range(4):
            next_r = cur_r
            next_c = cur_c
            
            while not check_wall(next_r, next_c, i):
                next_r += dr[i]
                next_c +=  dc[i]
                
                if board[next_r][next_c]!=0:
                    break
          
            
            if dp_dists[next_r][next_c] > dp_dists[cur_r][cur_c] + 1:
                dp_dists[next_r][next_c] = dp_dists[cur_r][cur_c] + 1
                stack.append((next_r, next_c))

    return dp_dists[to_r][to_c]

def print_M(M):
    for m in M:
        print(m)


def SearchCardOrder(board, card_history, start_r, start_c):

    stack = [(new2d(board), new2d(card_history), start_r, start_c, 0)]
    min_move = float("inf")
    while stack:
        board, card_history, cur_r, cur_c, move = stack.pop()
        print(board, card_history)
        print("-----------------")
        
        if check_board_clear(board):
            if min_move>move:
                min_move = move
            continue
        
        # CLICK ENTER 반영후 원상복귀
        if board[cur_r][cur_c] !=0:
            card = board[cur_r][cur_c]
            if not (cur_r, cur_c) in card_history[card]:
                #flip
                card_history[card].append((cur_r, cur_c))
                
                if len(card_history)==2: # 2개 뒤집힌 겨우
                    for (x, y) in card_history[card]:
                        board[x][y] = 0   
                    stack.append((new2d(board), new2d(card_history), cur_r, cur_c, move + 1))
                    # 복구
                    for (x, y)  in card_history[card]:
                        board[x][y] = card
                else: # 1개 뒤집힌 경우
                    stack.append((new2d(board), new2d(card_history), cur_r, cur_c, move + 1))
            # 복구
            card_history[card].pop()           

        # 그냥 움직인경우:
        for i in range(4):
            next_r = cur_r + dr[i]
            next_c = cur_c + dc[i]
            if 0<=next_r<4 and 0<= next_c<4:
                stack.append((new2d(board), new2d(card_history), next_r, next_c, move + 1))
            
        # CTRL MOVE
        for i in range(4):
            next_r = cur_r  + dr[i]
            next_c = cur_c  + dc[i]
            
            while 0<=next_r<4 and 0<= next_c<4 and board[next_r][next_c]==0:
                next_r += dr[i]
                next_c += dc[i]    
            if 0<=next_r<4 and 0<= next_c<4:
                stack.append((new2d(board), new2d(card_history), next_r, next_c, move + 1))
                
    return min_move

def solution(board, r, c):
    answer = 0
    card_history = []
    
    for i in range(0, 7):
        card_history.append([])

    for i in range(0, 7):
        card_history.append([])
    
    
    return DFS(board, card_history, r, c)


if __name__ == "__main__":
    print(solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]], 1, 0))
    # print(solution([[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]], 0, 1))
