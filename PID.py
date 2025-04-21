# https://drive.google.com/drive/folders/1syk5cGVZJzoWMIU9orpyWPuDMZ0Y8NyE?usp=sharing
# Map Cho Các Bạn Test

import numpy as np
import time
    
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

PID(error=XXX, p=X, i=X, d=X)