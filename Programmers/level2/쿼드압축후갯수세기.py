cnt = [0, 0]

def checksame(arr):
    target = arr[0][0]
    for ar in arr: # row
        for a in ar:
            if target==a:
                pass
            else:
                return False
    
    return True
    
def dfs(arr):
    global cnt
    N = len(arr)
    
    # check
    if checksame(arr):
        target = arr[0][0]
        cnt[target] -= N*N - 1 
        return
    
    half = N//2
    dfs([a[:half] for a in arr[:half]])
    dfs([a[:half] for a in arr[half:]])
    dfs([a[half:] for a in arr[:half]])
    dfs([a[half:] for a in arr[half:]])
    
    

def solution(arr):
    global cnt, N
    
    for ar in arr: # row
        for a in ar:
            if a==1:
                cnt[1] += 1
            else:
                cnt[0] += 1
    
    dfs(arr)   
    return cnt


if __name__ == "__main__":
    print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))