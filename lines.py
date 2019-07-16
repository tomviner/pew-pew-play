import pew
import random


pew.init()

screen = pew.Pix()

WIDTH = screen.width
HEIGHT = screen.height


def get_intermediate_points(a, b):
    dx = b[0] - a[0]
    dy = b[1] - a[1]
    deltas = [dx, dy]

    long_axis = int(abs(dy) > abs(dx))
    short_axis = 1 - long_axis

    d_long = deltas[long_axis]
    d_short = deltas[short_axis]

    # gradient
    m = d_short / d_long
    sign = int(d_long / abs(d_long))

    # count the long axis offset, either up or down:
    # --> 1, 2 ... d_long-2, d_long-1
    # --> -1, - 2 ... d_long+2, d_long+1
    for i in range(sign, d_long, sign):
        p = [None, None]
        p[long_axis] = a[long_axis] + i
        p[short_axis] = a[short_axis] + round(i * m)
        yield p


def check(p):
    if not 0 <= p[0] < WIDTH or not 0 <= p[1] < HEIGHT:
        import pdb
        pdb.set_trace()
    return p


def rotate(p, clwise=True):
    x, y = p
    dx, dy = 0, 0

    # skew and slide dividing line, so corners end up in opposite segments
    top_right = 0.9 * x > y - 0.2
    bottom_right = 1.1 * x > WIDTH - 1 - y + 0.2

    # print('top_right' if top_right else 'bottom_left')
    # print('bottom_right' if bottom_right else 'top_left')

    if top_right:
        if bottom_right:
            dy = clwise
        else:
            dx = clwise
    else:
        if bottom_right:
            dx = -clwise
        else:
            dy = -clwise

    return check([x + dx, y + dy])


def random_point(c, d=None):
    while d is None or c == d:
        d = [random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1)]
    check(d)
    return d


def count(n=0):
    while True:
        yield n
        n += 1


def draw_round(p, q):
    for i in count():
        pew.keys()
        p = rotate(p)
        check(p)

        if p == q:
            continue

        mids = list(get_intermediate_points(p, q))

        screen.box(color=0)

        screen.pixel(*p, color=3)
        screen.pixel(*q, color=3)

        for j, m in enumerate(mids):
            c = (j % 3) + 1
            screen.pixel(*m, color=c)

        pew.show(screen)
        pew.tick(1 / 32)

        # after a few iterations, randomly swap the points
        if i > 10 and not random.randint(0, 30):
            return q, p


def main():
    p = [0, 0]
    q = random_point(p)

    while True:
        p, q = draw_round(p, q)


if __name__ == '__main__':
    main()
