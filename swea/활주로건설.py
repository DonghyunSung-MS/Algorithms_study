import sys
sys.stdin = open("활주로건설.txt", "r")

T = int(input())
def possible(arr,x):
    cnt = 1
    bef = arr[0]
    for i in range(1,len(arr)):
        if arr[i] < bef: # 내리막
            if bef-arr[i] > 1:
                return 0
            else:
                if i+x > len(arr):
                    return 0
                else:
                    for j in range(i,i+x): #앞을 본다
                        if arr[j] != arr[i]:
                            return 0
                    cnt = -x+1
        elif arr[i] > bef: # 오르막
            if arr[i]-bef > 1:
                return 0
            else:
                if cnt >= x:
                    cnt = 1
                else:
                    return 0
        else:
            cnt+=1
        bef = arr[i]
    return 1

for test in range(T):
    N,X = map(int,input().split())
    mat = []
    for i in range(N):
        mat.append(list(map(int,input().split())))
    sol = 0
    for i in mat:
        sol+=possible(i,X)
    for i in zip(*mat): #전치행렬
        sol+=possible(i,X)
    print('#%d'%(test+1),sol)