# make cand and check prime number 2^n

# 유클리드 호제법으로 최대공약수 나보다 sqrt()까지 확인해서 배수가 있는지(p, r)<=1소수 p,r>=2

# 중복 없게 table 활용(hash?)

def gcd(a, b):
    while a>b:
        a = a-b

        if a<b:
            tmp = a
            b = a
            a = tmp

    return b


def make_candidates(seq, n):
    if n==0:
        return [""]

    results = []
    for i in range(len(seq)):
        m = seq[i]
        res = seq[:i]+ seq[i+1:]
        for sub in make_candidates(res, n-1):
            results.append(m+sub)

    return results

def check_prim(num):
    if num<2:
        return False

    until = int(num**0.5)

    for t in range(2, until + 1):
        if (num%t==0):
            return False

    return True


def solution(numbers):
    cands = []
    for i in range(1, len(numbers)+1):
        cands += make_candidates(numbers, i)
    table = {}
    for cand in cands:
        num = int(cand)
        if check_prim(num):
            table[num] = 1

    return len(table.keys())

if __name__ == "__main__":
    print(solution("17"))
    # print(gcd(1000000, 2))