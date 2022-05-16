# next - cur<=k
# 0 이면 다음 가장 가까운 곳
# 1씩감소
def check_possible(stones, minus, k):
    cnt = 1

    for stone in stones:
        delta = stone - minus
        if delta <= 0:
            cnt +=1
        else:
            if cnt>k:
                return False

            cnt = 1

    if cnt > k:
        return False
    return True



def solution(stones, k):
    a = 0  # True # 조건에서 1이상 배열
    b = max(stones)  # False

    # a m b
    # m True -> (m, b)
    # m False -> (a, m)
    # binary search O(logN)
    # check_possible O(N)
    # Total N*logN

    while a+1 < b:
        m = int((a + b) / 2)
        result = check_possible(stones, m, k)
        if result:
            a = m
        else:
            b = m

    return b

if __name__ == "__main__":
    print(solution([2, 5, 1, 1, 1, 1], 3))
    print(solution([2, 5, 1, 1, 1, 1], 4))
    print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
    print(solution([2, 4, 3, 5, 2, 1, 4, 2, 5, 1], 3))


