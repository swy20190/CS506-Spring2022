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
    raise NotImplementedError()

# Feel free to add more
