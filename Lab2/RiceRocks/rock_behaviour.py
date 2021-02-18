import numpy as np

CANVAS_RES = (800, 600)
PERCEPTION_RADIUS = 100
MAX_SPEED = 4
MAX_FORCE = 0.1


def edge(current):
    current.pos[0] %= CANVAS_RES[0]
    current.pos[1] %= CANVAS_RES[1]


def native_array(array):
    np_array = np.array(array)
    return [np_array[0].item(), np_array[1].item()]


def max_force(vec):
    if np.linalg.norm(vec) > MAX_FORCE:
        return (vec / np.linalg.norm(vec)) * MAX_FORCE
    return vec


def max_speed(vec):
    if np.linalg.norm(vec) > 0:
        return (vec / np.linalg.norm(vec)) * MAX_SPEED


def flock_vectors(current, boids):
    alignment = np.array([0, 0])
    cohesion = np.array([0, 0])
    separation = np.array([0, 0])
    total = 0
    for other in boids:
        diff = np.array(other.pos) - np.array(current.pos)
        dist = np.linalg.norm(diff)
        if other is not current and dist < PERCEPTION_RADIUS:
            alignment = np.add(alignment, np.array(other.vel))

            cohesion = np.add(cohesion, np.array(other.pos))

            diff_vec = np.subtract(np.array(current.pos), np.array(other.pos))
            diff_vec = np.divide(diff_vec, dist) if dist != 0 else diff_vec
            separation = np.add(separation, np.array(diff_vec))

            total += 1
    if total > 0:
        alignment = np.divide(alignment, total)
        alignment = (alignment / np.linalg.norm(alignment)) * MAX_SPEED
        alignment = np.subtract(alignment, np.array(current.vel))

        cohesion = np.divide(cohesion, total)
        cohesion = np.subtract(cohesion, np.array(current.pos))
        cohesion = max_speed(cohesion)
        cohesion = np.subtract(cohesion, np.array(current.vel))
        cohesion = max_force(cohesion)

        separation = np.divide(separation, total)
        separation = max_speed(separation)
        separation = np.subtract(separation, np.array(current.vel))
        separation = max_force(separation)

    return alignment, cohesion, separation


def attack(rock_position, rock_velocity, rock_acceleration, current, ship, missiles):
    missiles_list = list(missiles)
    attack_direction = np.subtract(ship.pos, current.pos)
    if len(missiles_list) > 0:
        attack_direction = np.subtract(missiles_list[0].pos, current.pos)

    attack_direction = max_speed(attack_direction)
    attack_direction = np.subtract(attack_direction, np.array(current.vel))
    attack_direction = max_force(attack_direction)

    attack_direction = native_array(attack_direction)
    if attack_direction != [0, 0]:
        rock_acceleration = native_array(attack_direction)

    rock_position = np.add(rock_position, rock_velocity)
    rock_velocity = np.add(rock_velocity, rock_acceleration)

    return rock_position, rock_velocity


def defense(rock_position, rock_velocity, rock_acceleration, current, ship, missiles):
    missiles_list = list(missiles)
    defense_direction = np.subtract(current.pos, ship.pos)
    if len(missiles_list) > 0:
        defense_direction = np.subtract(current.pos, missiles_list[0].pos)

    defense_direction = max_speed(defense_direction)
    defense_direction = np.subtract(defense_direction, np.array(current.vel))
    defense_direction = max_force(defense_direction)

    defense_direction = native_array(defense_direction)
    if defense_direction != [0, 0]:
        rock_acceleration = native_array(defense_direction)

    rock_position = np.add(rock_position, rock_velocity)
    rock_velocity = np.add(rock_velocity, rock_acceleration)

    return rock_position, rock_velocity


def update_rock_position(current, boids, ship, missiles):
    acceleration = [0, 0]
    alignment, cohesion, separation = flock_vectors(current, boids)

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

    # by default CALM behaviour is used
    no_missiles = len(missiles)
    # if there are less than 3 missiles the attack behaviour is used
    if 0 < no_missiles <= 3:
        position, velocity = attack(position, velocity, acceleration, current, ship, missiles)
    # if there are mote than 3 missiles then defense behaviour is used
    elif no_missiles > 3:
        position, velocity = defense(position, velocity, acceleration, current, ship, missiles)

    current.pos = native_array(position)
    current.vel = native_array(velocity)

    edge(current)
