def huh3(rr):
    rrc = rr[:]
    i = 0
    while i < len(rrc) - 1:
        m = i
        for j in range(i, len(rrc)):
            if rrc[m] > rrc[j]:
                m = j
        rrc[i], rrc[m] = rrc[m], rrc[i]
        i += 1
    return rrc      