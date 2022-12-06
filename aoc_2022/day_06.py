
def marker(seq: str, n=4):
    last_n = []
    for i, x in enumerate(seq):
        last_n.append(x)
        if len(last_n) > n:
            last_n.pop(0)
        if len(last_n) == len(set(last_n)) == n:
            return i + 1