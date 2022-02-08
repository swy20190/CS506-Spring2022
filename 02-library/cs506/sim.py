def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    if len(x)==0 or len(y)==0:
        raise ValueError("lengths must not be zero")
    if len(x) != len(y):
        raise ValueError("lengths must be equal")
    res = 0
    for i in range(len(x)):
        res += abs(x[i]-y[i])
    return res

def jaccard_dist(x, y):
    if len(x)==0 or len(y)==0:
        raise ValueError("lengths must not be zero")
    f1 = 0
    x = list(set(x))
    for i in x:
        if i in y:
            f1 += 1
    f2 = len(set(x+y))

    return 1-f1/f2

def cosine_sim(x, y):
    if len(x)==0 or len(y)==0:
        raise ValueError("lengths must not be zero")

    if len(x) != len(y):
        raise ValueError("lengths must be equal")

    f1 = 0
    sqx = 0
    sqy = 0
    for i in range(len(x)):
        f1 += x[i]*y[i]
        sqx += x[i]**2
        sqy += y[i]**2

    return f1/((sqx**(1/2))*(sqy**(1/2)))


# Feel free to add more
