def ceil(a, d):
    return -int(-a//d)

# this is wrong ceilling
# when a < 0 it goes wrong because when a<0 int(a/d) is ceil not floor
def ceil2(a, d):
    if a%d==0:
        return int(a/d)
    else:
        return int(a/d)+1

        
def time2min(time):
    return int(time[:2])*60 + int(time[3:])

MAXTIME = time2min("23:59")

def solution(fees, records):
    intimes = dict() #(intime) out del
    cumtimes = dict()
    
    for record in records:
        time, carnum, status = record.split(" ")
        if status=="IN":
            intimes[carnum] = time2min(time)
        
        else:
            outtime = time2min(time)
            intime = intimes[carnum]
            if carnum in cumtimes:
                cumtimes[carnum] += outtime - intime
            else:
                cumtimes[carnum]  = outtime - intime
            del intimes[carnum]
    
    # 안나간 차량 최대시간 계산
    for carnum, intime in intimes.items():
        outtime = MAXTIME
        if carnum in cumtimes:
            cumtimes[carnum] += outtime - intime
        else:
            cumtimes[carnum]  = outtime - intime

    ans = []
    for carnum, cumtime in cumtimes.items():
        # 기본요금 + max((누적시간 - 기본시간)/단위시간 * 단위요금, 0)
        fee = fees[1] + max(ceil(cumtime - fees[0], fees[2]) * fees[3], 0)        
        ans.append((carnum, fee))
    
    ans.sort(key=lambda x:x[0])       
    
    answer = [int(fee) for car, fee in ans]
    return answer

if __name__ == "__main__":
    print(ceil(0, 3))
    print(ceil2(-1, 3))