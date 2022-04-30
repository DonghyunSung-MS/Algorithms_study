import  sys
sys.stdin = open("숫자만들기.txt", "r")

N = None
max_ans = None
min_ans = None


def dfs(depth, add_cnt, sub_cnt, mul_cnt, div_cnt, source_tuple, prev_result):
    global max_ans, min_ans

    if depth>=N:
        if prev_result > max_ans:
            max_ans = prev_result
        if prev_result < min_ans:
            min_ans = prev_result
        return

    if add_cnt > 0:
        dfs(depth + 1, add_cnt - 1, sub_cnt, mul_cnt, div_cnt, source_tuple, prev_result + source_tuple[depth]) # depth 1, 2
    if sub_cnt > 0:
        dfs(depth + 1, add_cnt, sub_cnt-1, mul_cnt, div_cnt, source_tuple, prev_result - source_tuple[depth])  # depth 1, 2
    if mul_cnt > 0:
        dfs(depth + 1, add_cnt, sub_cnt, mul_cnt-1, div_cnt, source_tuple, prev_result * source_tuple[depth])  # depth 1, 2
    if div_cnt > 0:
        dfs(depth + 1, add_cnt, sub_cnt, mul_cnt, div_cnt-1, source_tuple, int(prev_result / source_tuple[depth]))  # depth 1, 2


def solve():
    global  N, min_ans,max_ans
    min_ans = float("inf")
    max_ans = -float("inf")

    N = int(input())
    # add sub mul div
    add_cnt, sub_cnt, mul_cnt, div_cnt = map(int, input().split())
    source_tuple = tuple(map(int, input().split()))

    dfs(1, add_cnt, sub_cnt, mul_cnt, div_cnt, source_tuple, source_tuple[0])

    return max_ans - min_ans


if __name__ == "__main__":
    T = int(input())
    for test_case in range(1,T+1):
        ans = solve()
        print(f"#{test_case} {ans}")
