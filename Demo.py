# https://drive.google.com/drive/folders/1syk5cGVZJzoWMIU9orpyWPuDMZ0Y8NyE?usp=sharing
# Map Cho Các Bạn Test

import socket
import cv2
import numpy as np
import time
import json
import base64

global sendBack_angle, sendBack_Speed, current_speed, current_angle, radius
sendBack_angle = 0
sendBack_Speed = 0
current_speed = 0
current_angle = 0
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
PORT = 54321
s.connect(('127.0.0.1', PORT))

def Control(angle, speed):
    global sendBack_angle, sendBack_Speed
    sendBack_angle = angle
    sendBack_Speed = speed
    
error_arr = np.zeros(5)
pre_t = time.time()
MAX_SPEED = 60

def PID(error, p, i, d):
    global pre_t, error_arr
    error_arr[1:] = error_arr[0:-1]
    error_arr[0] = error
    P = error * p
    delta_t = time.time() - pre_t
    pre_t = time.time()
    if delta_t != 0:
        D = (error - error_arr[1]) / delta_t * d
    else:
        D = 0
    I = np.sum(error_arr) * delta_t * i
    angle = P + I + D
    if abs(angle) > 25:
        angle = np.sign(angle) * 25
    return int(angle)

if __name__ == "__main__":
    try:
        while True:
            message = bytes(f"{sendBack_angle} {sendBack_Speed}", "utf-8")
            s.sendall(message)
            data = s.recv(100000)
            data_recv = json.loads(data)
            current_angle = data_recv["Angle"]
            current_speed = data_recv["Speed"]
            jpg_original = base64.b64decode(data_recv["Img"])
            jpg_as_np = np.frombuffer(jpg_original, dtype=np.uint8)
            image = cv2.imdecode(jpg_as_np, flags=1)
            angle_setpoint = PID(error=XXX, p=X, i=X, d=X)
            print(current_speed, current_angle)
            # cv2.imshow('Image Original', image)
            Control(angle_setpoint, 10)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        print('closing socket')
        s.close()