import sys
sys.stdin = open("원자소멸.txt", "r")

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def solve1():
    ####################### get input and init setting
    N = int(input())
    atoms = [] # x, y, dir, energy
    total_energy = 0
    for i in range(N):
        atoms.append(tuple(map(int, input().split())))

    # simulate step 0.5 sec
    # while len(atoms) >= 2:
    for t in range(5000): # 이것도 가능
        # move O(N)

        for i in range(len(atoms)):
            x, y, dir_idx, k = atoms[i]
            x = x + 0.5 * dx[dir_idx]
            y = y + 0.5 * dy[dir_idx]
            atoms[i] = (x, y, dir_idx, k)


        # 현재 atom의 위치를 파악 O(N)
        atom_xy_map = {}
        for atom in atoms:
            x, y, dir_idx, k = atom
            if (x, y) in atom_xy_map.keys():
                atom_xy_map[(x, y)].append((dir_idx, k))
            else:
                atom_xy_map[(x, y)] = [(dir_idx, k)]


        # 해당 위치에 몇개 있는지 파악 O(N*K(충돌)) 충둘은 N보다 매우 작을 경우가 많음.
        atoms = []
        for (x, y), xy_atoms in atom_xy_map.items():
            if len(xy_atoms)>1: #두 마리 이상
                for xy_atom in xy_atoms:
                    total_energy += xy_atom[1]
            else:
                if -1000<=x<=1000 and -1000<=y<=1000: ######################### 시간 초과 방지를 위해서 매우 중요
                    dir_idx, k = xy_atoms[0]
                    atoms.append((x, y, dir_idx, k))

        ########### # check collision O(N^2) fail
        # tmp_atoms = []
        # for i in range(len(atoms)):
        #     i_alive = True
        #     for j in range(len(atoms)):
        #         if i!=j: #서로 다른 쌍에 대하여
        #             # i 기준으로만 생각하기
        #             xi, yi, _, k = atoms[i]
        #             xj, yj, _, _ = atoms[j]
        #             if xi==xj and yi==yj: # 충돌
        #                 i_alive = False
        #                 break
        #     if i_alive:
        #         tmp_atoms += [atoms[i]]
        #     else:
        #         total_energy += atoms[i][3]
        # # atoms 초기화
        # atoms = []
        # atoms.extend(tmp_atoms)

    return total_energy


if __name__ == "__main__":
    T = int(input())
    for test_case in range(1, T + 1):
        ans = solve1()
        print(f"#{test_case} {ans}") # 제출 형식 주의