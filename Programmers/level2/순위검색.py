def bs(seq, target):
    s = 0
    e = len(seq)

    while s < e:
        m = (s + e) // 2

        if seq[m] >= target:
            e = m
        else:
            s = m + 1

    return len(seq) - s

print(bs([0, 1,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,4,5],3))