import time

class MRB_PID:
    def __init__(self):
        self.kp = 0
        self.ki = 0
        self.kd = 0

        self.i_term = 0

        self.out_min = None
        self.out_max = None

        self.setpoint = None

        self.last_time = time.time()
        self.sample_time = 0.1

        self.last_input = 0
        self.last_output = None

    def set_output_limits(self, lower, higher):
        self.out_min = lower
        self.out_max = higher

        if self.i_term > self.out_max:
            self.i_term = self.out_max
        elif self.i_term < self.out_min:
            self.i_term = self.out_min

    def set_tunings(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki * self.sample_time
        self.kd = kd / self.sample_time

    def set_setpoint(self, setpoint):
        self.setpoint = setpoint

    def set_sample_time(self, sample_time):
        ratio = sample_time / self.sample_time
        self.ki *= ratio
        self.kd /= ratio
        self.sample_time = sample_time

    def compute(self, _input):
        time_difference = time.time() - self.last_time
        if time_difference < self.sample_time:
            print("Sample time not passed. Returning previous output.")
            return self.last_output

        error = self.setpoint - _input
        self.i_term += self.ki * error
        if self.i_term > self.out_max:
            self.i_term = self.out_max
        elif self.i_term < self.out_min:
            self.i_term = self.out_min
        d_input = _input - self.last_input

        output = self.kp * error + self.i_term - self.kd * d_input

        if output > self.out_max:
            output = self.out_max
        elif output < self.out_min:
            output = self.out_min

        self.last_time = time.time()
        self.last_input = _input
        self.last_output = output

        return output
