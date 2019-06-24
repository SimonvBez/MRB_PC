import MRB_Constants
import time
import cv2
import numpy as np
import imutils
import PIL.ImageTk
import PIL.Image
import threading
import MRB_Serial
import MRB_linear_algebra
import serial


class MRB_Controller():
    def __init__(self):
        self.lower_orange = np.array([13, 63, 255])
        self.upper_orange = np.array([21, 255, 255])

        self.hsv = None
        self.video_cap = None
        self.gui = None
        self.servo_offsets = [0] * 3
        self.servo_positions = [(None, None)] * 3
        self.servo_calibration_counter = 0
        self.ball_destination = (None, None)
        self.ball_position = (None, None)
        self.arduino = None

    def set_gui(self, gui):
        self.gui = gui

    def set_servo_percentages_with_offset(self, servo_values):
        self.arduino.set_servo_percentages([servo_values[i] + self.servo_offsets[i] for i in range(3)])

    def window_click(self, event):
        select_mode = self.gui.get_select_mode()
        if select_mode == MRB_Constants.BALL_COLOR_CALIBRATION:
            hsv_pixel = self.hsv[event.y, event.x]
            self.lower_orange = (hsv_pixel - np.array([4, 100, 30])).clip(0, 255)
            self.upper_orange = (hsv_pixel + np.array([4, 255, 255])).clip(0, 255)
        elif select_mode == MRB_Constants.SELECT_SERVO_POS:
            if not self.servo_calibration_counter:
                self.servo_positions = [(None, None)] * 3
            self.servo_positions[self.servo_calibration_counter] = (event.x, event.y)
            self.servo_calibration_counter += 1
            if self.servo_calibration_counter == 3:
                self.servo_calibration_counter = 0
        elif select_mode == MRB_Constants.SELECT_BALL_DEST:
            self.ball_destination = (event.x, event.y)

    def cam_thread(self):
        self.video_cap = cv2.VideoCapture(0)

        while True:
            if self.video_cap.isOpened():
                ret, bgr = self.video_cap.read()

                bgr_blur = cv2.GaussianBlur(bgr, (5, 5), 0)
                self.hsv = cv2.cvtColor(bgr_blur, cv2.COLOR_BGR2HSV)
                mask = cv2.inRange(self.hsv, self.lower_orange, self.upper_orange)
                mask = cv2.erode(mask, None, iterations=4)
                mask = cv2.dilate(mask, None, iterations=4)

                contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                contours = imutils.grab_contours(contours)

                # Find and draw ball position
                if len(contours) > 0:
                    c = max(contours, key=cv2.contourArea)
                    ((x, y), radius) = cv2.minEnclosingCircle(c)
                    M = cv2.moments(c)
                    center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
                    if radius > 10:
                        self.ball_position = center
                        cv2.circle(bgr, (int(x), int(y)), int(radius), (0, 255, 255), 2)
                        cv2.circle(bgr, center, 5, (0, 0, 255), -1)

                # Draw servo positions
                for i in range(len(self.servo_positions)):
                    if self.servo_positions[i][0] is not None:
                        text_position = list(self.servo_positions[i])
                        text_position[0] -= 10
                        text_position[1] += 10
                        text_position = tuple(text_position)
                        cv2.putText(bgr, str(i + 1), text_position, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

                # Draw ball destination
                if self.ball_destination[0] is not None:
                    cv2.circle(bgr, self.ball_destination, 10, (60, 255, 0), 2)

                mask = cv2.resize(mask, None, fx=0.5, fy=0.5)

                # Put it all in the GUI
                rgb_photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)))
                mask_photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(mask))
                self.gui.get_top().Webcam.create_image(0, 0, image=rgb_photo, anchor='nw')
                self.gui.get_top().Webcam.obr = rgb_photo
                self.gui.get_top().Webcam_mask.create_image(0, 0, image=mask_photo, anchor='nw')
                self.gui.get_top().Webcam_mask.orb = mask_photo
                self.gui.get_top().Webcam.bind("<Button 1>", self.window_click)
            else:
                time.sleep(0.2)

    def gui_thread(self):
        t1 = threading.Thread(target=self.cam_thread)
        t1.setDaemon(True)
        t1.start()

        self.arduino = MRB_Serial.MRB_Serial()
        self.gui.set_connected(True)
        while True:
            try:
                self.servo_offsets = self.gui.get_servo_offsets()
                state = self.gui.get_program_state()

                if state == MRB_Constants.STATE_ACTIVE:
                    self.set_servo_percentages_with_offset([0, 0, 0])
                    # if (None, None) not in self.servo_positions and self.ball_destination != (None, None) and self.ball_position != (None, None):
                    #     print(MRB_linear_algebra.calculate_distance_per_servo(self.servo_positions, self.ball_position, self.ball_destination))

                    time.sleep(0.1)
                elif state == MRB_Constants.STATE_CALIBRATION:
                    self.set_servo_percentages_with_offset([100, 100, 100])
                    time.sleep(0.05)
                elif state == MRB_Constants.STATE_IDLE:
                    self.arduino.reset_servos()
                    time.sleep(0.2)

            except (serial.serialutil.SerialException, serial.serialutil.SerialTimeoutException):
                self.gui.set_connected(False)
                time.sleep(1)
                self.arduino.wait_for_connection()
                self.gui.set_connected(True)

    def gui_task(self):
        self.gui.get_root().after(50, self.gui_task)
