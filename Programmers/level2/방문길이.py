def solution(dirs):
    visited = dict()
    
    
    cx = 0
    cy = 0
    
    for dir in dirs:
        if dir=="U":
            nx = cx
            ny = cy + 1
        elif dir=="D":
            nx = cx
            ny = cy - 1
        elif dir=="L":
            nx = cx - 1 
            ny = cy
        elif dir=="R":
            nx = cx + 1 
            ny = cy
            
        
        if -5<=nx<=5 and -5<=ny<=5:
            visited[(nx, ny, cx, cy)] = 1
            visited[(cx, cy, nx, ny)] = 1
        
            cx = nx
            cy = ny
            
    return len(visited.keys())//2