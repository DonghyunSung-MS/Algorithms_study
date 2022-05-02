import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while True:
        if scoville[0] >= K:
            break

        try:
            heapq.heappush(scoville, heapq.heappop(scoville)+heapq.heappop(scoville)*2)
        except:
            return -1

        answer += 1

    return answer

if __name__ == "__main__":
    print(solution([1,2],7))