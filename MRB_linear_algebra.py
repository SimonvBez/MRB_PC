import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def init_from_list(cls, a):
        return cls(a[0], a[1])

    @classmethod
    def init_from_list_list(cls, a):
        result = []
        for p in a:
            result.append(Point.init_from_list(p))
        return result

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


def get_effective_servo_angles(angle_list, compare_angle):
    difference_list = []
    result = []
    largest_angle = 0
    for angle in angle_list:
        difference_list.append(angle_difference(angle, compare_angle))
        if difference_list[-1] > largest_angle:
            largest_angle = difference_list[-1]

    for i, angle in enumerate(difference_list):
        if angle < largest_angle:
            result.append([i, angle_list[i]])

    return result


def calculate_distance_per_servo(servo_positions, ball_position, ball_destination):
    servo_positions = Point.init_from_list_list(servo_positions)
    servo_angles = []

    # Get the effective angles of each servo
    for i in range(len(servo_positions)):
        servo_point = servo_positions[i]
        cross_point = midpoint(servo_positions[:i] + servo_positions[i + 1:])

        servo_angles.append(angle_between(cross_point, servo_point))

    ball_position = Point.init_from_list(ball_position)
    ball_destination = Point.init_from_list(ball_destination)
    ball_roll_distance = distance_between(ball_position, ball_destination)

    roll_angle = angle_between(ball_position, ball_destination)

    # Check if the servo must move down in order to make the ball get to its destination
    effective_servo_angles = get_effective_servo_angles(servo_angles, roll_angle)
    # effective_servo_angles_old = []
    # for i in range(len(servo_angles)):
    #     if servo_is_effective(servo_angles[i], roll_angle):
    #         effective_servo_angles_old.append([i, servo_angles[i]])

    result = [0.0] * 3
    if len(effective_servo_angles) == 2:
        servo1 = effective_servo_angles[0]
        servo2 = effective_servo_angles[1]

        ball_distance_opp_corner = 180 - angle_difference(roll_angle, servo1[1]) - angle_difference(roll_angle, servo2[1])

        servo1_length = ball_roll_distance * (math.sin(math.radians(angle_difference(roll_angle, servo2[1]))) / math.sin(math.radians(ball_distance_opp_corner)))
        servo2_length = ball_roll_distance * (math.sin(math.radians(angle_difference(roll_angle, servo1[1]))) / math.sin(math.radians(ball_distance_opp_corner)))

        result[servo1[0]] = servo1_length
        result[servo2[0]] = servo2_length
    elif len(effective_servo_angles) == 1:
        result[effective_servo_angles[0][0]] = ball_roll_distance

    return result
