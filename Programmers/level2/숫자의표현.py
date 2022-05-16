def solution(n):
    # O(sqrt(N))
    answer = 0
    n = 2*n
    for i in range(1, int(n**0.5)+1):
        if n % i==0:
            a = n/i
            b = i
            if (a+b)%2==1:
                answer += 1
    
    
    return answer


def solution2(n):
    # O(N*K)
    answer = 0
    for start in range(1, n+1):
        sums = 0
        while sums<n:
            sums += start
            start+=1
        
        if n==sums:
            answer += 1
    
    
    return answer