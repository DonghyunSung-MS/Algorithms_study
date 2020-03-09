def solution(progresses, speeds):
    done_day = []
    for (a,b) in zip(progresses, speeds):
        a = 100 - a
        tmp = a//b if a%b==0 else a//b+1
        done_day.append(tmp)
    print(done_day)
    answer = []
    done_day = done_day[::-1]
    current_day = done_day.pop()
    task_cnt = 0
    while True:
        next_day = done_day[-1]
        if current_day>=next_day:
            done_day.pop()
            task_cnt+=1
        else:
            current_day = done_day.pop()
            answer.append(task_cnt)
            task_cnt=0

    return answer

if __name__=='__main__':
    progresses = [93,30,55]
    speeds = [1,30,5]
    print(solution())
