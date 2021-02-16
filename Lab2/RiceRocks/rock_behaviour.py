import numpy as np
import random

CANVAS_RES = (800, 600)
PERCEPTION_RADIUS = 150
ACCELERATION = 0.01
LIMIT = 800
VELOCITY_DIVIDER = 1.2


def normalize(v):
    norm = np.linalg.norm(v)
    if norm == 0:
        return v
    return v / norm


def edges(current):
    current.pos[0] %= CANVAS_RES[0]
    current.pos[1] %= CANVAS_RES[1]


def native_array(array):
    np_array = np.array(array)
    return [np_array[0].item(), np_array[1].item()]


def align(current, boids):
    steering = np.array([0, 0])
    total = 0
    for other in boids:
        diff = np.array(other.pos) - np.array(current.pos)
        dist = np.linalg.norm(diff)
        if other is not current and dist < PERCEPTION_RADIUS:
            steering = np.add(steering, np.array(other.vel))
            total += 1
    if total > 0:
        steering = np.divide(steering, total)
        steering = np.subtract(steering, np.array(current.vel))
    return steering


def cohesion(current, boids):
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
        steering = np.subtract(steering, np.array(current.pos))
        steering = np.subtract(steering, np.array(current.vel))
    return steering


def flock(current, boids):
    if not hasattr(current, 'acc'):
        # current.acc = [random.randrange(-1, 2), random.randrange(-1, 2)]
        current.acc = [0, 0]

    alignment = align(current, boids)
    cohesion_ = cohesion(current, boids)

    total = np.add(np.array(current.acc), alignment)
    total = np.add(total, cohesion_)

    total = native_array(total)
    if total != [0, 0]:
        current.acc = native_array(total)


def update_rock_position(current, boids):
    flock(current, boids)

    position = np.array(current.pos)
    velocity = np.array(current.vel)
    acceleration = np.array(current.acc)

    print(position, velocity, acceleration)

    position = np.add(position, velocity)
    velocity = np.add(velocity, acceleration)
    velocity = normalize(velocity)
    current.acc = [0, 0]

    current.pos = native_array(position)
    current.vel = native_array(velocity)

    edges(current)
