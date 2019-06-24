import serial
import serial.tools.list_ports
import time


class MRB_Serial:
    def __init__(self):
        self.ser = serial.Serial()
        self.ser.baudrate = 2400
        # self.ser.setDTR(0)
        self.wait_for_connection()
        self.servo_times = [None] * 16

    def __del__(self):
        self.close()

    @staticmethod
    def int_list2bytes(int_list):
        result = b''
        for i in range(len(int_list)):
            result += int_list[i].to_bytes(2, byteorder='big')
        return result

    def close(self):
        if self.ser.is_open:
            self.ser.close()

    def wait_for_connection(self):
        self.close()
        while True:
            for ser_device in serial.tools.list_ports.comports():
                if "Arduino Due Programming Port" in ser_device.description:
                    self.ser.port = ser_device.device
                    self.ser.open()
                    time.sleep(0.5)
                    return
            time.sleep(1)

    def send_serial_command(self, cmd_bytes):
        self.ser.write(b'Cmd' + cmd_bytes)

    def reset_servos(self):
        if self.servo_times != [None] * 16:
            self.send_serial_command(b'R')
            self.servo_times = [None] * 16

    def set_servo(self, servo_num, end_time):
        if 0 <= end_time <= 4095 and 0 <= servo_num <= 15:
            if end_time != self.servo_times[servo_num]:
                self.send_serial_command(b'S' + bytes([servo_num]) + end_time.to_bytes(2, byteorder='big'))
                self.servo_times[servo_num] = end_time

    def set_servos(self, end_times):
        if max(end_times) <= 4095 and min(end_times) >= 0 and len(end_times) == 3:
            if end_times != self.servo_times:
                self.send_serial_command(b'A' + self.int_list2bytes(end_times))
                self.servo_times = end_times

    def set_servo_percentage(self, servo_num, percentage):
        self.set_servo(servo_num, 550 - int(percentage * 1.0))

    def set_servo_percentages(self, percentages):
        end_times = []
        for i in range(len(percentages)):
            end_times.append(540 - int(percentages[i] * 1.0))
        self.set_servos(end_times)
