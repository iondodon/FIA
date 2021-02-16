import numpy as np

CANVAS_RES = (800, 600)
PERCEPTION_RADIUS = 150
ACCELERATION = 0.01
LIMIT = 800
VELOCITY_DIVIDER = 1.2


def native_array(np_array):
    return [np_array[0].item(), np_array[1].item()]


def align(current, boids):
    steering = np.array([0, 0])
    total = 0
    for other in boids:
        diff = np.array(other.pos) - np.array(current.pos)
        dist = np.linalg.norm(diff)
        if other is not current and dist < PERCEPTION_RADIUS:
            steering = np.add(steering, np.array(other.pos))
            total += 1
    if total > 0:
        steering = np.divide(steering, total)
        steering = np.subtract(steering, np.array(current.vel))
    return steering


def flock(current, boids):
    alignment = align(current, boids)
    alignment = np.divide(alignment, LIMIT)
    current.acc = native_array(alignment)


def update_rock_position(current, boids):
    flock(current, boids)

    position = np.array(current.pos)
    velocity = np.array(current.vel)
    acceleration = np.array(current.acc)

    position = np.add(position, velocity)
    velocity = np.add(velocity, acceleration)
    velocity = np.divide(velocity, VELOCITY_DIVIDER)

    current.pos = native_array(position)
    current.vel = native_array(velocity)
    current.acc = native_array(acceleration)

    current.pos[0] %= CANVAS_RES[0]
    current.pos[1] %= CANVAS_RES[1]
