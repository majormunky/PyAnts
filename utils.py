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


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return str("{}, {}".format(self.x, self.y))

    def __iter__(self):
        return [self.x, self.y]

    def __getitem__(self, key):
        if key not in [0, 1]:
            raise KeyError
        if key == 0:
            return self.x
        elif key == 1:
            return self.y
