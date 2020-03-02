def solution(n):
    #3 (6,9,12) (15,18,21,24,27,30,33,36,39)
    # 8/3 = 2 --- 2
    # 2
    x = ['4', '1', '2'] #나머지
    ans = ""
    while n>0:
        ans+=x[n%3]
        if n%3==0:
            n=n-1
        n = n//3
    ans = ans[::-1]
    return ans


if __name__=="__main__":
    ns = [x+1 for x in range(30)]
    for n in ns:
        print(n,' | ',solution(n))
