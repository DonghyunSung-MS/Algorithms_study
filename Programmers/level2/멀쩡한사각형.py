def solution(w,h):
    #최대공약수 G
    #w=Gm, h=Gn
    #유클리드
    a = max(w,h)
    b = min(w,h)
    G = -1
    while True:
        c = a%b #나머지
        if c==0:
            G = b
            break
        a = max(b,c)
        b = min(b,c)
    print(G)
    m = w//G
    n = h//G
    #(m+n)-1
    white = m + n - 1
    answer = w*h - white*G
    return answer
