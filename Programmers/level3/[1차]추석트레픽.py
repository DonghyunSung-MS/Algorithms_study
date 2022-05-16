def line2abms(line):
    # line 2016-09-15 01:00:04.001 s
    _, time, sec = line.split(" ")
    del_msec = None
    if "." in sec:
        a, b = sec[:-1].split(".")
        del_msec = int(a)*1000 + int(b)
    else:
        sec = int(sec[:-1])
        del_msec = sec * 1000

    h, m, s = time.split(":")
    a, b = s.split(".")
    time_msec = 60 * 60 * 1000 * int(h) + 60 * 1000 * int(m) + 1000 * int(a) + int(b)

    start = time_msec - del_msec + 1
    end = time_msec
    return start, end


def solution(lines):
    answer = 0

    ms_lines_se = []
    for line in lines:
        s, e = line2abms(line)
        ms_lines_se.append([s, e])

    N = len(lines)
    for i in range(N):
        cnt = 0
        for j in range(i, N):
            # end time(i) > start time(j) - 1000
            if ms_lines_se[i][1] > ms_lines_se[j][0] - 1000:
                cnt +=1

        answer = max(answer, cnt)

    print(answer)
    return answer

if __name__ == "__main__":
    solution( [
        "2016-09-15 01:00:04.001 2.0s",
        "2016-09-15 01:00:07.000 2s"
    ])
    solution([
        "2016-09-15 01:00:04.002 2.0s",
        "2016-09-15 01:00:07.000 2s"]
    )

    solution([
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
])