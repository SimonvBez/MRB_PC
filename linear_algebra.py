import numpy as np
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def init_from_list(cls, a):
        return cls(a[0], a[1])

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __truediv__(self, other):
        return Point(self.x / other, self.y / other)

    def __repr__(self):
        return str([self.x, self.y])

    def list(self):
        return [self.x, self.y]


def midpoint(positions):
    return (positions[0] + positions[1]) / 2


def angle_between(p1, p2):
    xDiff = p2.x - p1.x
    yDiff = p2.y - p1.y
    return math.degrees(math.atan2(yDiff, xDiff))


def distance_between(p1, p2):
    xDiff = p2.x - p1.x
    yDiff = p2.y - p1.y
    return math.sqrt(xDiff ** 2 + yDiff ** 2)


def angle_difference(a1, a2):
    return 180 - abs(abs(a1 - a2) - 180)


def servo_is_effective(servo_angle, ball_angle):
    angle = angle_difference(servo_angle, ball_angle)
    return angle < 90


servo_positions = [Point(400, 400), Point(300, 200), Point(500, 200)]
servo_angles = []

for i in range(len(servo_positions)):
    servo_point = servo_positions[i]
    cross_point = midpoint(servo_positions[:i] + servo_positions[i+1:])

    servo_angles.append(angle_between(cross_point, servo_point))

ball_point = Point(400, 400)
desired_point = Point(400, 455)
ball_roll_distance = distance_between(ball_point, desired_point)

ball_angle = angle_between(ball_point, desired_point)
effective_servo_angles = []

for i in range(len(servo_angles)):
    if servo_is_effective(servo_angles[i], ball_angle):
        print("Servo {} is effective".format(i))
        effective_servo_angles.append([i, servo_angles[i]])
    else:
        print("Servo {} is not effective".format(i))

if len(effective_servo_angles) == 2:
    servo1 = effective_servo_angles[0]
    servo2 = effective_servo_angles[1]

    ball_distance_opp_corner = 180 - angle_difference(ball_angle, servo1[1]) - angle_difference(ball_angle, servo2[1])

    servo1_length = ball_roll_distance * (math.sin(math.radians(angle_difference(ball_angle, servo2[1]))) / math.sin(math.radians(ball_distance_opp_corner)))
    servo2_length = ball_roll_distance * (math.sin(math.radians(angle_difference(ball_angle, servo1[1]))) / math.sin(math.radians(ball_distance_opp_corner)))

    print("Servo {}: {}".format(servo1[0], servo1_length))
    print("Servo {}: {}".format(servo2[0], servo2_length))
elif len(effective_servo_angles) == 1:
    print("Servo {}: {}".format(effective_servo_angles[0][0], ball_roll_distance))
