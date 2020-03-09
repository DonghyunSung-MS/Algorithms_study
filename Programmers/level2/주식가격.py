from collections import deque

def solution(prices):
    prices = deque(prices)
    answer = []
    while prices:
        current = prices.popleft() #list.pop(0) O(n) // deque.popleft() O(1)
        cnt = 0
        for p in prices:
            cnt+=1
            if p<current:
                break
        answer.append(cnt)
    return answer


if __name__=='__main__':
    prices = [1, 2, 3, 2, 3]
    print(solution())
