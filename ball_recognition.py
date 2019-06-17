import cv2
import numpy as np
import imutils


def recalibrate(event, x, y, flags, param):
    global lower_orange
    global upper_orange
    if event == cv2.EVENT_LBUTTONDOWN:
        hsv_color = hsv[y, x]
        lower_orange = (hsv_color - np.array([4, 100, 30])).clip(0, 255)
        upper_orange = (hsv_color + np.array([4, 255, 255])).clip(0, 255)
        print(lower_orange)
        print(upper_orange)


cap = cv2.VideoCapture(0)
cv2.namedWindow("frame", cv2.WINDOW_NORMAL)
cv2.setMouseCallback("frame", recalibrate)

lower_orange = np.array([13, 63, 255])
upper_orange = np.array([21, 255, 255])

while True:
    if cap.isOpened():
        _, rgb = cap.read()
        rgb_blur = cv2.GaussianBlur(rgb, (5, 5), 0)

        hsv = cv2.cvtColor(rgb_blur, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower_orange, upper_orange)
        mask = cv2.erode(mask, None, iterations=4)
        mask = cv2.dilate(mask, None, iterations=4)
        output = cv2.bitwise_and(rgb_blur, rgb_blur, mask=mask)

        contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = imutils.grab_contours(contours)
        center = None

        # only proceed if at least one contour was found
        if len(contours) > 0:
            # find the largest contour in the mask, then use
            # it to compute the minimum enclosing circle and
            # centroid
            c = max(contours, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

            # only proceed if the radius meets a minimum size
            if radius > 10:
                # draw the circle and centroid on the frame,
                # then update the list of tracked points
                cv2.circle(rgb_blur, (int(x), int(y)), int(radius), (0, 255, 255), 2)
                cv2.circle(rgb_blur, center, 5, (0, 0, 255), -1)

        cv2.imshow('frame', rgb_blur)
        cv2.imshow('mask', mask)
        cv2.imshow('output', output)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print("Error opening VideoCapture.")

cap.release()
cv2.destroyAllWindows()
