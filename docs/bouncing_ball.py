import pew


pew.init()
screen = pew.Pix()
ball = pew.Pix.from_iter((
    (3, 2),
    (2, 1),
))
background = pew.Pix.from_iter((
    (1, 0, 1, 0, 1, 0, 1, 0),
    (0, 1, 0, 1, 0, 1, 0, 1),
    (1, 0, 1, 0, 1, 0, 1, 0),
    (0, 1, 0, 1, 0, 1, 0, 1),
    (1, 0, 1, 0, 1, 0, 1, 0),
    (0, 1, 0, 1, 0, 1, 0, 1),
    (1, 0, 1, 0, 1, 0, 1, 0),
    (0, 1, 0, 1, 0, 1, 0, 1),
))
x = 3
y = 1
dx = 1
dy = 1
while True:
    keys = pew.keys()
    screen.blit(background)
    if not 0 < x < 6 or keys & pew.K_O:
        dx = -dx
    if not 0 < y < 6 or keys & pew.K_X:
        dy = -dy
    x += dx
    y += dy
    screen.blit(ball, x, y)
    pew.show(screen)
    pew.tick(1/12)