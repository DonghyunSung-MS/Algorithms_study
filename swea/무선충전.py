import sys
sys.stdin = open("무선충전.txt", "r")

# 최대 충전 계산
def max_perform(ax,ay,bx,by,board, BC_perf):
    # 같은 영향권에 있는지 -> 같은 bc idx 가 있는지
    a_bc_idx = board[(ax,ay)]
    b_bc_idx = board[(bx, by)]

    # 4가지 케이스
    if len(a_bc_idx)==0 and len(b_bc_idx)==0:
        return 0.0
    # 하나만 충전이면 최대하면됨
    elif len(a_bc_idx)>0 and len(b_bc_idx)==0:
        tmp_charges = [BC_perf[idx] for idx in a_bc_idx]
        return max(tmp_charges)
    elif len(a_bc_idx) ==0 and len(b_bc_idx) > 0:
        tmp_charges = [BC_perf[idx] for idx in b_bc_idx]
        return max(tmp_charges)

    elif len(a_bc_idx) > 0 and len(b_bc_idx) > 0: # 둘다 존재
        # BC 겹치는게 있는지 고려하여 최대 조합
        max_ch = -float("inf")
        for a_idx in a_bc_idx:
            for b_idx in b_bc_idx:
                each_charge = 0.0
                if a_idx == b_idx:
                    each_charge = BC_perf[a_idx]
                else:
                    each_charge = BC_perf[a_idx] + BC_perf[b_idx]

                if each_charge>max_ch:
                    max_ch = each_charge
        return max_ch

def solve():
    ################ Create Board
    # board[(x,y)] = [bc_idx] 영향을 미치는 지역별로 performance
    board = {}
    for x in range(10):
        for y in range(10):
            board[(x+1, y+1)] = []


    # M는 이동시간, A는 BC의 갯수
    M, A = map(int, input().split())
    a_moves = list(map(int, input().split()))
    b_moves = list(map(int, input().split()))
    BC_perf = []
    for bc_idx in range(A):
        x, y, c, p = map(int, input().split())
        BC_perf.append(p)
        #local c x c 그리드에서 베터리 영향권 입력
        for dx in range(2*c+1):
            for dy in range(2*c+1):
                tmp_x = x + dx - c
                tmp_y = y + dy - c
                dist = abs(tmp_x - x) + abs(tmp_y - y)
                if 1<=tmp_x<=10 and 1<=tmp_y<=10 and dist<=c:
                    board[(tmp_x, tmp_y)].append(bc_idx)

    # 각 최대 충전 계산
    total_charge = 0
    ax = 1
    ay = 1
    bx = 10
    by = 10

    total_charge += max_perform(ax, ay, bx, by, board, BC_perf) # at T=0

    dX = [0, 0, 1, 0, -1]
    dY = [0, -1, 0, 1, 0]

    for t in range(M):
        ax += dX[a_moves[t]]
        ay += dY[a_moves[t]]

        bx += dX[b_moves[t]]
        by += dY[b_moves[t]]

        total_charge += max_perform(ax, ay, bx, by, board, BC_perf)  # at T=t
    return  total_charge

if __name__ == "__main__":
    T = int(input())
    # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
    for test_case in range(1, T + 1):
        ans = solve()
        print(f"#{test_case} {int(ans)}")