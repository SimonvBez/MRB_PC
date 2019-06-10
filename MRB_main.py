import MRB_Serial
import MRB_GUI
import time
import serial


def my_thread(gui):
    controller = MRB_Serial.MRB_Controller()
    gui.set_connected()

    while True:
        try:
            # controller.set_servo_percentage(1, 100 + gui.get_top().Ser1_scale.get())
            # controller.set_servo_percentage(2, 100 + gui.get_top().Ser2_scale.get())
            # controller.set_servo_percentage(3, 100 + gui.get_top().Ser3_scale.get())
            controller.set_servo_percentages([100, 100, 100])

            time.sleep(0.5)
        except (serial.serialutil.SerialException, serial.serialutil.SerialTimeoutException):
            gui.set_disconnected()
            time.sleep(1)
            controller.wait_for_connection()
            gui.set_connected()


def my_task(gui):
    gui.get_root().after(1000, my_task, gui)


if __name__ == '__main__':
    MRB_GUI.MRB_GUI(my_task, my_thread)
