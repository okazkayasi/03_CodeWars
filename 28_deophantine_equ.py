import math
def sol_equa(n):


    # first one must be lower than sqrt and second one must be greater
    # x > 2*y
    # find a and b first
    # b is one on one off
    # a

    # find all integer divisions
    l = []
    sq = int(math.ceil(math.sqrt(n)))

    for i in range(1, sq+1):
            if n%i == 0:
                l.append([i, n/i])

    print l
    ret = []
    for each in l:
        if (each[0] + each[1]) % 2 == 0:
            x = (each[0] + each[1]) / 2
            if (each[1] - x) % 2 == 0:
                y = (each[1] - x)/2
                ret.append([x,y])

    return ret

print sol_equa(16)
