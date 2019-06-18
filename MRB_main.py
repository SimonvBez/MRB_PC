import MRB_Serial
import MRB_GUI
import time
import serial
import threading
import cv2
import numpy as np
import imutils
import PIL.ImageTk
import PIL.Image


def window_click(event):
    global lower_orange
    global upper_orange
    global hsv
    global select_state

    if select_state.get() == "Ball Calibration":
        hsv_color = hsv[event.y, event.x]
        lower_orange = (hsv_color - np.array([4, 100, 30])).clip(0, 255)
        upper_orange = (hsv_color + np.array([4, 255, 255])).clip(0, 255)
    elif select_state.get() == "Servo Calibration":
        print("Servo cal")
    elif select_state.get() == "Ball position":
        print("Ball pos")


def cam_thread(gui):
    global lower_orange
    global upper_orange
    global hsv
    global select_state
    select_state = gui.get_top().selection_mode

    cap = cv2.VideoCapture(0)

    lower_orange = np.array([13, 63, 255])
    upper_orange = np.array([21, 255, 255])

    while True:
        if cap.isOpened():
            ret, bgr = cap.read()

            bgr_blur = cv2.GaussianBlur(bgr, (5, 5), 0)
            hsv = cv2.cvtColor(bgr_blur, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(hsv, lower_orange, upper_orange)
            mask = cv2.erode(mask, None, iterations=4)
            mask = cv2.dilate(mask, None, iterations=4)

            contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            contours = imutils.grab_contours(contours)

            if len(contours) > 0:
                c = max(contours, key=cv2.contourArea)
                ((x, y), radius) = cv2.minEnclosingCircle(c)
                M = cv2.moments(c)
                center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
                if radius > 10:
                    cv2.circle(bgr, (int(x), int(y)), int(radius), (0, 255, 255), 2)
                    cv2.circle(bgr, center, 5, (0, 0, 255), -1)

            mask = cv2.resize(mask, None, fx=0.5, fy=0.5)

            rgb_photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)))
            mask_photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(mask))
            gui.get_top().Webcam.create_image(0, 0, image=rgb_photo, anchor='nw')
            gui.get_top().Webcam.obr = rgb_photo
            gui.get_top().Webcam_mask.create_image(0, 0, image=mask_photo, anchor='nw')
            gui.get_top().Webcam_mask.orb = mask_photo
            gui.get_top().Webcam.bind("<Button 1>", window_click)
        else:
            time.sleep(0.2)


def gui_thread(gui):
    t1 = threading.Thread(target=cam_thread, args=[gui])
    t1.setDaemon(True)
    t1.start()

    controller = MRB_Serial.MRB_Controller()
    gui.set_connected()

    while True:
        try:
            servo_offsets = (gui.get_top().Ser1_scale.get(), gui.get_top().Ser2_scale.get(), gui.get_top().Ser3_scale.get())
            state = gui.get_top().state.get()

            if state == "Active":
                controller.set_servo_percentages([100 + servo_offsets[0], 100 + servo_offsets[1], 100 + servo_offsets[2]])
                time.sleep(0.1)
            elif state == "Calibration":
                controller.set_servo_percentages([0 + servo_offsets[0], servo_offsets[1], servo_offsets[2]])
                time.sleep(0.1)
            elif state == "Idle":
                controller.reset_servos()
                time.sleep(0.5)

        except (serial.serialutil.SerialException, serial.serialutil.SerialTimeoutException):
            gui.set_disconnected()
            time.sleep(1)
            controller.wait_for_connection()
            gui.set_connected()


def gui_task(gui):
    # Enables the servo offset scales when in Calibration mode
    new_state = gui.get_top().state.get()
    old_state = gui.get_top().previous_state
    if new_state != old_state:
        if new_state == "Calibration":
            gui.get_top().Ser1_scale.config(state="normal")
            gui.get_top().Ser2_scale.config(state="normal")
            gui.get_top().Ser3_scale.config(state="normal")
        else:
            gui.get_top().Ser1_scale.config(state="disabled")
            gui.get_top().Ser2_scale.config(state="disabled")
            gui.get_top().Ser3_scale.config(state="disabled")

    gui.get_top().previous_state = new_state

    gui.get_root().after(50, gui_task, gui)


if __name__ == '__main__':
    MRB_GUI.MRB_GUI(gui_task, gui_thread)
