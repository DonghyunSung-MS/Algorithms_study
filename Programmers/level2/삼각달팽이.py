def solution(n):
    answer = []
    total = int(n * (n+1)/2)
    
    board = [[0]*n for _ in range(n)]
    
    num = 1
    row = 0
    col = 0
    while num <= total:
        # down
        while  0<=row<n and 0<=col<n and board[row][col]==0:
            board[row][col] = num
            num +=1
            row +=1

        row-=1
        col+=1
        
        # left
        while  0<=row<n and 0<=col<n and board[row][col]==0:
            board[row][col] = num
            col += 1
            num += 1
        col-=2
        row-=1
        
        # diag up
        while  0<=row<n and 0<=col<n and board[row][col]==0:
            board[row][col] = num
            col -= 1
            row -= 1
            num += 1
            
        col+=1
        row+=2
                   
    for rows in board:
        for ele in rows:
            if ele !=0:
                answer.append(ele)
    return answer

print(solution(6))