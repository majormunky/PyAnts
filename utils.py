import math


def get_distance(pos1, pos2):
    return math.sqrt(((pos2[0] - pos1[0]) ** 2) + ((pos2[1] - pos1[1]) ** 2))


def get_angle(origin, target):
    dx = target[0] - origin[0]
    dy = target[1] - origin[1]
    rads = math.atan2(-dy, dx)
    rads %= 2 * math.pi
    degs = math.degrees(rads)
    return int(degs)
