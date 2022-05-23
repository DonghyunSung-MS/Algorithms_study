NUM = ord("Z") - ord("A") + 1

MIN_CURSOR = float("inf")

def check_all_zero(arr):
    for a in arr:
        if a ==0:
            pass
        else:
            return False
    return True
    

def dfs(loc, cursor, depth):
    global MIN_CURSOR
    if depth > len(cursor):
        return    
    
    if check_all_zero(cursor):
        # print(loc, cursor, depth)

        if MIN_CURSOR > depth:
            MIN_CURSOR = depth
        return
    

    
    
    tmp_cursor = cursor[:]
    tmp_cursor[loc] = 0
    
    dfs((loc + 1) % len(cursor) , tmp_cursor, depth + 1)
    dfs((loc - 1) % len(cursor) , tmp_cursor, depth + 1)
    
    
    

def solution(name):
    diff = []
    for char in name:
        diff.append(min(ord(char) - ord("A"), ord("A") - ord(char) +  NUM))
    
    cursor = []
    for d in diff:
        if d>0:
            cursor.append(1)
        else:
            cursor.append(0)
    dfs(0, cursor, 0)
    answer = sum(diff) + MIN_CURSOR - 1
    
    # 아무것도 안해도될때 오류 해결
    if check_all_zero(cursor):
        answer += 1
    
    return answer