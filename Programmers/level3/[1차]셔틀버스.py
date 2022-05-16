# 콘은 제일 늦게 타려함
# 같은 시간도 뒤에

# 셔틀 시간
# [9:00, 09:00 + t,  n*(t-1)] n개 막차
# 최대 nxm 명
def string2minute(time):
    return int(time[:2]) * 60 + int(time[3:])


def minute2string(minute):
    h = minute // 60
    m = minute % 60
    return f"{h:02d}:{m:02d}"


def solution(n, t, m, timetable):
    table_minutes = [string2minute(time) for time in timetable]
    shutles = [string2minute("09:00") + i * t for i in range(n)]
    table_minutes.sort()

    shutle_to_crew_time = []

    crew_idx = 0
    for shutle in shutles:
        cnt = 1
        tmp = []
        # 셔틀 >= 손님시간 cnt<=m
        while cnt <= m and crew_idx<len(timetable) and shutle >= table_minutes[crew_idx]:
            tmp.append(table_minutes[crew_idx])
            cnt += 1
            crew_idx += 1

        shutle_to_crew_time.append(tmp)

    # 가장 마지막 시간 셔틀에 끼어 들어가기?
    # 안되는 예외가 있나 있어 -> 크루가 모두 최소 [1,1,1, 1,1,1, 1,1,1, 1,1,1] 셔틀의 갯수가 딱 맞으면 어쩔수 없이 첫차를 타야함.
    # 뒷차부터 가능한지 조사
    answer = None
    shutle = shutles[-1]
    crew_times = shutle_to_crew_time[-1]

    if len(crew_times)<m:
        answer = minute2string(shutle)
    else: # 같으면 문제
        # crew_times <= shutle
        set_crew_time = list(set(crew_times))
        answer = minute2string(set_crew_time[-1]-1)


    print(answer)
    print("=================")
    return answer

if __name__ == "__main__":
    # solution(5,	1,	1,	["00:01", "00:01", "00:01", "00:01", "00:01"])

    solution(1,	1,	5,	["08:00", "08:01", "08:02", "08:03"])
    solution(2,	10,	2,	["09:10", "09:09", "08:00"])
    solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"])#  "08:59"
    solution(1,	1,	5,	["00:01", "00:02", "00:03", "00:04", "00:05"])
    solution(1,	1,	1,	["23:59"])
    solution(10, 60, 45, ["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"])