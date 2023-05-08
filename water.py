import RPi.GPIO as GPIO
import time

# pin number
flow_sen_1 = 17
flow_sen_2 = 27
flow_sen_3 = 22

# var 
flow_sen_1_time = 0
flow_sen_2_time = 0
flow_sen_3_time = 0

flow_sen_1_time_p = 0
flow_sen_2_time_p = 0
flow_sen_3_time_p = 0

flow_sen_1_del_time = 0
flow_sen_2_del_time = 0
flow_sen_3_del_time = 0

flow_sen_1_freq = 0
flow_sen_2_freq = 0
flow_sen_3_freq = 0

flow_sen_1_data = 0
flow_sen_2_data = 0
flow_sen_3_data = 0
"""
def time_to_millis():
    time_now = time.time()
    time_now = (int(time_now * 1000))
    return time_now

def flow_sen_1_int(self):
    flow_sen_1_time = time_to_millis()

def flow_sen_2_int(self):
    flow_sen_2_time = time_to_millis()

def flow_sen_3_int(self):
    flow_sen_3_time = time_to_millis()
    
"""

def flow_sen_1_int(self):
    global flow_sen_1_time
    time_now = time.time()
    time_now = (int(time_now * 1000))

    flow_sen_1_time = time_now

def flow_sen_2_int(self):
    global flow_sen_2_time
    time_now = time.time()
    time_now = (int(time_now * 1000))

    flow_sen_2_time = time_now

def flow_sen_3_int(self):
    global flow_sen_3_time
    time_now = time.time()
    time_now = (int(time_now * 1000))

    flow_sen_3_time = time_now



GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(flow_sen_1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(flow_sen_2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(flow_sen_3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(flow_sen_1, GPIO.RISING, callback=flow_sen_1_int)
GPIO.add_event_detect(flow_sen_2, GPIO.RISING, callback=flow_sen_2_int)
GPIO.add_event_detect(flow_sen_3, GPIO.RISING, callback=flow_sen_3_int)

while True:
    
    # print("running 1")

    if flow_sen_1_time != flow_sen_1_time_p:
        flow_sen_1_del_time = flow_sen_1_time - flow_sen_1_time_p
        flow_sen_1_del_time = flow_sen_1_del_time / 1000
        flow_sen_1_freq = 1 / flow_sen_1_del_time
        flow_sen_1_val = flow_sen_1_freq / 5.50
        # equal to Liter per minute
        # change to mL per minute
        flow_sen_1_val = int(flow_sen_1_val * 1000)
        print("SENSOR 1 : ", end="")
        print(flow_sen_1_val)
        flow_sen_1_time_p = flow_sen_1_time
    
    # print("running  2")

    if flow_sen_2_time != flow_sen_2_time_p:
        flow_sen_2_del_time = flow_sen_2_time - flow_sen_2_time_p
        flow_sen_2_del_time = flow_sen_2_del_time / 1000
        flow_sen_2_freq = 1 / flow_sen_2_del_time
        flow_sen_2_val = flow_sen_2_freq / 5
        # equal to Liter per minute
        # change to mL per minute
        flow_sen_2_val = int(flow_sen_2_val * 1000)
        print("SENSOR 2 : ", end="")
        print(flow_sen_2_val)
        flow_sen_2_time_p = flow_sen_2_time
    
    # print("running   3")

    if flow_sen_3_time != flow_sen_3_time_p:
        flow_sen_3_del_time = flow_sen_3_time - flow_sen_3_time_p
        flow_sen_3_del_time = flow_sen_3_del_time / 1000
        flow_sen_3_freq = 1 / flow_sen_3_del_time
        flow_sen_3_val = flow_sen_3_freq / 7.50
        # equal to Liter per minute
        # change to mL per minute
        flow_sen_3_val = int(flow_sen_3_val * 1000)
        print("SENSOR 3 : ", end="")
        print(flow_sen_3_val)
        flow_sen_3_time_p = flow_sen_3_time

    # print("running    4")
