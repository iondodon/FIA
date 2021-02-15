import numpy as np

CANVAS_RES = (800, 600)
DIMENSIONS = 2
PERCEPTION_RADIUS = 100
MAX_FORCE = 1


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
    current.acc = [alignment[0].item(), alignment[1].item()]


def update_rock_position(current, boids):
    flock(current, boids)

    position = np.array(current.pos)
    velocity = np.array(current.vel)
    acceleration = np.array(current.acc)

    position = np.add(position, velocity)
    velocity = np.add(velocity, acceleration)
    velocity = np.divide(velocity, 600)

    current.pos = [position[0].item(), position[1].item()]
    current.vel = [velocity[0].item(), velocity[1].item()]
