import math


def get_distance(pos1, pos2):
    return math.sqrt(((pos2[0] - pos1[0]) ** 2) + ((pos2[1] - pos1[1]) ** 2))


def get_angle(origin, target):
    dx = target.x - origin.x
    dy = target.y - origin.y
    rads = math.atan2(-dy, dx)
    rads %= 2 * math.pi
    degs = math.degrees(rads)
    return int(degs)
