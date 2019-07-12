import pew

WIDTH = 8
HEIGHT = 8

pew.init()

screen = pew.Pix()

p = [WIDTH - 1, HEIGHT - 1]

def get_mids(a, b):
    dx = b[0] - a[0]
    dy = b[1] - a[1]
    ds = [dx, dy]

    long_axis = int(abs(dy) > abs(dx))
    short_axis = int(not long_axis)

    d_long = ds[long_axis]
    d_short = ds[short_axis]

    m = d_short / d_long
    print('m', m)
    sign = int(d_long / abs(d_long))

    p = [None, None]
    i = 0
    for _ in range(abs(d_long) - 1):
        i += sign
        p[long_axis] = a[long_axis] + round(i)
        p[short_axis] = a[short_axis] + round(i * m)
        yield list(p)

while True:
    for sign in (-1, 1):
        for axis_pos in (0, 1):
            for i in range(WIDTH - 1):
                p[axis_pos] += sign

                q = (WIDTH - p[0] - 1, HEIGHT - p[1] - 1)

                mids = list(get_mids(p, q))

                screen.box(color=0)
                pew.show(screen)

                screen.pixel(*p, color=3)
                screen.pixel(*q, color=3)

                for m in mids:
                    print(m)
                    screen.pixel(*m, color=2)

                pew.show(screen)
                pew.tick(1/8)
