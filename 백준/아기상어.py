"""
아기상어 위치 9
물고기 크기 (1~6)
0 빈칸

상어가 자라는 조건 크기만큼 물고기 섭취
물고기는 작으면 먹을 수 있고 같은 면 지나갈 수 있고,
크면 못먹어

맵에서 못먹으면 엄마 호출.
"""
from collections import deque
N = None
space = None

def get_input():
    global N, space
    
    N = int(input())
    space = []
    for i in range(N):
        space.append(list(map(int, input().split())))
    
def get_shark_loc():
    for i in range(N): # row
        for j in range(N): # col
            if space[i][j] == 9:
                return i, j

def get_zero_mat():
    tmp = []
    for i in range(N):
        tmp.append([0]* N)
    return tmp

def bfs(start, shark_size):
    i, j = start
    distance = get_zero_mat()
    visited = get_zero_mat()
    
    queue = deque([(i, j)])
    visited[i][j] = 1
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]
    results = []
    while queue:
        cur_i, cur_j = queue.popleft()
        for index in range(4):
            nex_i = cur_i + di[index]
            nex_j = cur_j + dj[index]
            # with in boundary and not visited and fish is smaller or equal to shark size to bypass
            if 0<=nex_i<N and 0<=nex_j<N and not visited[nex_i][nex_j] and space[nex_i][nex_j] <= shark_size:
                queue.append((nex_i, nex_j)) # add queue
                visited[nex_i][nex_j] = 1 # check visit
                distance[nex_i][nex_j] = distance[cur_i][cur_j] + 1 # distance
                
                if space[nex_i][nex_j] < shark_size and 0<space[nex_i][nex_j] <=6:
                    # if there is smaller fish than shark eat
                    results+=[(nex_i, nex_j, distance[nex_i][nex_j])]
    
    # return closest fish > upper > left
    return sorted(results, key=lambda x: (x[2], x[0], x[1]))
                
  
if __name__ == "__main__":
    get_input()
    i, j = get_shark_loc()
    
    shark_size = 2
    cnt = 0
    time = 0
    
    while True:
        results = bfs((i,j), shark_size)
        if len(results) ==0:
            break
        
        result = results[0]
        
        time += result[2]
        
        space[i][j] = 0
        space[result[0]][result[1]] = 0
        
        i, j = result[0], result[1]
        
        cnt += 1 
        
        if cnt == shark_size:
            cnt = 0
            shark_size+=1
            
    print(time)