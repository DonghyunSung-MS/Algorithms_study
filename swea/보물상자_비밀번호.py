import sys
sys.stdin = open("보물상자_비밀번호.txt", "r")

'''
16진수 (0~F)
'''
from collections import deque


def todigit(n):
    length = len(n)
    sum = 0
    for i in range(length):
        tmp = n[i]
        idx = length - 1 - i
        if tmp.isdigit():
            sum += (16**idx)*int(tmp)
        else: #ABCDEF
            sum += (16**idx)*(ord(tmp) - ord("A") + 10)

    return sum

def solve():
    N, K = map(int, input().split())
    one_cycle = N//4

    char_list = list(input())
    que = deque(char_list)
    source_list = []
    for _ in range(one_cycle):
        # move one cyle
        x = que.pop()
        que.appendleft(x)

        char_list = list(que)

        for i in range(4):
            d16 = char_list[one_cycle*i:one_cycle*(i+1)]
            d10 = todigit(d16)
            source_list.append(d10)

    source_list = list(set(source_list))
    source_list.sort(reverse=True)

    return source_list[K-1]




if __name__ == "__main__":
    T = int(input())
    for test_case in range(1,T+1):
        ans = solve()
        print(f"#{test_case} {ans}")