from collections import deque


def solution(rows, columns, queries):
    answer = []
    board = [[0] * columns for _ in range(rows)]
    # make board
    num = 1
    for i in range(rows):
        for j in range(columns):
            board[i][j] = num
            num += 1

    for (i, j, k, l) in queries:
        i -= 1
        j -= 1
        k -= 1
        l -= 1

        # 회전 index 최소값 구하기
        tmp_number = []  # 고정
        idx_deque = deque()
        for idx in range(j, l):  # (i,j) ~ (i, l-1)
            idx_deque.append((i, idx))
            tmp_number.append(board[i][idx])

        for idx in range(i, k):  # (i,l) ~ (k-1, l)
            idx_deque.append((idx, l))
            tmp_number.append(board[idx][l])

        for idx in reversed(range(j + 1, l + 1)):  # (k,l) ~ (k, j+1)
            idx_deque.append((k, idx))
            tmp_number.append(board[k][idx])

        for idx in reversed(range(i + 1, k + 1)):  # (k,j) ~ (i+1, j)
            idx_deque.append((idx, j))
            tmp_number.append(board[idx][j])

        answer.append(min(tmp_number))

        # first to last clockwise
        idx_deque.append(idx_deque.popleft())
        # board 회전
        cnt = 0
        while idx_deque:
            ti, tj = idx_deque.popleft()
            board[ti][tj] = tmp_number[cnt]
            cnt += 1
    return answer

def print_M(M):
    for m in M:
        print(m)
    print("---------")


if __name__ == "__main__":
    solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]])