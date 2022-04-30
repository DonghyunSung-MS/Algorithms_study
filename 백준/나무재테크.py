'''
1부터 시작 주의

양분 5 만큼

M 나무

봄: 
    현양분 - 나이 성장 +1
    여러나무 나이 어린 나무 부터
    양분 못먹을시 즉사

여름:
    죽은나무 -> 양분 + 죽은나무//2
    
가을:
    나이%5==0 -> 인접지역 나이1 나무 생성

겨울:
    s2d2양분 추가 

살아있는 나무 갯수 출력.
# 1차 brute force 완료
# 2차 효율적으로?
# NxN ok 100개 max
# K linear 필수
# M 나무

# 제한 조건에서 주어지는 나무위치가 모두다름을 활용
'''

# 맵에 위치 alive dead

N,M,K=0,0,0
A = [] # 겨울추가양분
F = None
ATrees = None
DTrees = None

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def get_NxN_list():
    return [[[] for _ in range(N)] for _ in range(N)]

def get_input():
    global N, M, K, A, ATrees
    N, M, K = map(int, input().split())
    
    # get A
    for _ in range(N):
        A.append(list(map(int, input().split())))
    ATrees = get_NxN_list()
    
    for _ in range(M):# 위치 1부터 주의
        x, y, age = map(int, input().split()) # x, y, age
        ATrees[x - 1][y - 1].append(age)

# 10 x 10 x 100
def spring_summer():
    '''
    봄: 
    현양분 - 나이 성장 +1
    여러나무 나이 어린 나무 부터
    양분 못먹을시 즉사
    '''
    global DTrees
    DTrees = []
    for x in range(N):
        for y in range(N):
            length = len(ATrees[x][y])
            if length > 0: #살아있는 나무가 있다면
                ATrees[x][y].sort() 
                new_xy_tree = []
                xy_plus_F = 0
                for i in range(length):
                    if F[x][y] >= ATrees[x][y][i]:
                        F[x][y] -= ATrees[x][y][i] #양분을 먹고
                        ATrees[x][y][i] += 1 # 나이를 먹고
                        new_xy_tree.append(ATrees[x][y][i])
                    else:
                        xy_plus_F += ATrees[x][y][i]//2 # 죽은나무에넣고
                
                ATrees[x][y] = []
                ATrees[x][y].extend(new_xy_tree)
                F[x][y] += xy_plus_F

def fall_and_winter():
    '''
    가을:
    나이%5==0 -> 인접지역 나이1 나무 생성
    '''
    # 현재 존재 위치(x, y) + 새로생길 나무 x, y, age 모은후
    # 현재 위치가 존재하면 기존 node에 아니면 새로운 node 생성
    for x in range(N):
        for y in range(N):
            F[x][y] += A[x][y] # winter

            length = len(ATrees[x][y])
            if length > 0: #살아있는 나무가 있다면
                for i in range(length):
                    if ATrees[x][y][i]%5==0:
                        for idx in range(8):
                            loc_x = x + dx[idx]
                            loc_y = y + dy[idx]
                            if 0<=loc_x<N and 0<=loc_y<N:
                                ATrees[loc_x][loc_y].append(1)
        
            
if __name__ == "__main__":
    get_input()
    F = [[5 for _ in range(N)] for _ in range(N)] # 초기 양분
    
    for _ in range(K):
        spring_summer()
        fall_and_winter()
        
    # count 나무
    cnt = 0
    for x in range(N):
        for y in range(N):
            cnt += len(ATrees[x][y])
    
    print(cnt)