def time2sec(time):
    h, m, s = map(int, time.split(":"))

    return h * 3600 + m * 60 + s


def sec2time(sec):
    h = sec // 3600
    mm = sec % 3600

    m = mm // 60
    s = mm % 60

    return f"{h:02d}:{m:02d}:{s:02d}"


def solution(play_time, adv_time, logs):
    play_time = time2sec(play_time)
    adv_time = time2sec(adv_time)

    cummulative_watching = [0 for _ in range(play_time + 1)]  # 0~play_time
    for log in logs:
        start = time2sec(log[:8])
        end = time2sec(log[9:])
        cummulative_watching[start] += 1
        cummulative_watching[end] -= 1

    # 시청시간 채우기
    for i in range(play_time):
        cummulative_watching[i + 1] = cummulative_watching[i] + cummulative_watching[i + 1]  # i 누적시간 + i+1 시청시간

    # 누적시간
    for i in range(play_time):
        cummulative_watching[i + 1] = cummulative_watching[i] + cummulative_watching[i + 1]  # i 누적시간 + i+1 시청시간

    max_perfom = 0
    min_time = 0

    for i in range(0, play_time + 2 - adv_time):
        time = i
        # time ~ advtime+time
        if i == 0:  # 예외케이스
            perform = cummulative_watching[i + adv_time - 1]
        else:
            perform = cummulative_watching[i + adv_time - 1] - cummulative_watching[time - 1]

        if perform > max_perfom:
            min_time = time
            max_perfom = perform

    return sec2time(min_time)


if __name__ == "__main__":
    print(solution("02:03:55", "00:14:15",
                   ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29",
                    "01:37:44-02:02:30"]))