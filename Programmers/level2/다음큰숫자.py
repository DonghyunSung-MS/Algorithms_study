def counter(n):
    cnt = 0
    for ele in str(bin(n)):
        if ele == "1":
            cnt +=1
    return cnt


def solution(n):
    num1 = counter(n)
    while True:
        n = n + 1
        if num1 == counter(n):
            break
    return n

if __name__ == "__main__":
    print(solution(78))
    print(solution(15))