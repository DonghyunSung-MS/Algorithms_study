from collections import deque

def solution(priorities, location):
    deq = deque(priorities)
    current_max = max(deq)
    index = 0
    n = 0
    while True:
        tmp = deq.popleft()
        if tmp==current_max:
            n+=1
            current_max = max(deq) if deq else -1
            if location == 0:
                break
        else:
            deq.append(tmp)
        location = location -1 if location>0 else len(deq)-1
    return n

if __name__=="__main__":
    priorities = [1]
    location = 0
    print(solution(priorities, location))
