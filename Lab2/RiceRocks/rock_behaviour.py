import numpy as np

CANVAS_RES = (800, 600)
PERCEPTION_RADIUS = 100
MAX_SPEED = 3
MAX_FORCE = 0.2


def edge(current):
    current.pos[0] %= CANVAS_RES[0]
    current.pos[1] %= CANVAS_RES[1]


def native_array(array):
    np_array = np.array(array)
    return [np_array[0].item(), np_array[1].item()]


def flock_vectors(current, boids, ship):
    align_ = np.array([0, 0])
    cohesion_ = np.array([0, 0])
    separation_ = np.array([0, 0])
    total = 0
    for other in boids:
        diff = np.array(other.pos) - np.array(current.pos)
        dist = np.linalg.norm(diff)
        if other is not current and dist < PERCEPTION_RADIUS:
            align_ = np.add(align_, np.array(other.vel))

            cohesion_ = np.add(cohesion_, np.array(other.pos))

            diff_vec = np.subtract(np.array(current.pos), np.array(other.pos))
            diff_vec = np.divide(diff_vec, dist) if dist != 0 else diff_vec
            separation_ = np.add(separation_, np.array(diff_vec))

            total += 1
    if total > 0:
        align_ = np.divide(align_, total)
        align_ = (align_ / np.linalg.norm(align_)) * MAX_SPEED
        align_ = np.subtract(align_, np.array(current.vel))

        cohesion_ = np.divide(cohesion_, total)
        cohesion_ = np.subtract(cohesion_, np.array(current.pos))
        if np.linalg.norm(cohesion_) > 0:
            cohesion_ = (cohesion_ / np.linalg.norm(cohesion_)) * MAX_SPEED
        cohesion_ = np.subtract(cohesion_, np.array(current.vel))
        if np.linalg.norm(cohesion_) > MAX_FORCE:
            cohesion_ = (cohesion_ / np.linalg.norm(cohesion_)) * MAX_FORCE

        separation_ = np.divide(separation_, total)
        if np.linalg.norm(separation_) > 0:
            separation_ = (separation_ / np.linalg.norm(separation_)) * MAX_SPEED
        separation_ = np.subtract(separation_, np.array(current.vel))
        if np.linalg.norm(separation_) > MAX_FORCE:
            separation_ = (separation_ / np.linalg.norm(separation_)) * MAX_FORCE

    return align_, cohesion_, separation_


def update_rock_position(current, boids, ship):
    acceleration = [0, 0]
    alignment, cohesion, separation = flock_vectors(current, boids, ship)

    total = np.add(acceleration, alignment)
    total = np.add(total, cohesion)
    total = np.add(total, separation)
    total = native_array(total)
    if total != [0, 0]:
        acceleration = native_array(total)

    position = np.array(current.pos)
    velocity = np.array(current.vel)
    acceleration = np.array(acceleration)

    position = np.add(position, velocity)
    velocity = np.add(velocity, acceleration)

    # ///////////
    total_cohesion = np.subtract(ship.pos, current.pos)
    if np.linalg.norm(total_cohesion) > 0:
        total_cohesion = (total_cohesion / np.linalg.norm(total_cohesion)) * MAX_SPEED
    total_cohesion = np.subtract(total_cohesion, np.array(current.vel))
    if np.linalg.norm(total_cohesion) > MAX_FORCE:
        total_cohesion = (total_cohesion / np.linalg.norm(total_cohesion)) * MAX_FORCE

    total = np.add([0, 0], total_cohesion)
    total = native_array(total)
    if total != [0, 0]:
        acceleration = native_array(total)

    position = np.add(position, velocity)
    velocity = np.add(velocity, acceleration)
    # ///////////

    current.pos = native_array(position)
    current.vel = native_array(velocity)

    edge(current)
