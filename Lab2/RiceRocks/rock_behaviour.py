CANVAS_RES = (800, 600)
DIMENSIONS = 2


def update_rock_position(sprite):
    for i in range(DIMENSIONS):
        sprite.pos[i] %= CANVAS_RES[i]
        sprite.pos[i] += sprite.vel[i] * 5
