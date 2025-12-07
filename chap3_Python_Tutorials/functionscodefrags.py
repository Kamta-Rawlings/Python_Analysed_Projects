x = 5


def f(g):
    h = g * x
    return h


def g():
    global x
    x = 178


def h():
    global x
    x = 12
    return x


print(f(13), g(), f(13), f(h()))
