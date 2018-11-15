import subprocess

import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)


try:
    while True:
        input_state = GPIO.input(17)
        if input_state == 0:
            subprocess.call("fswebcam -d /dev/video0 -r 1024x768 -S20 " "/home/pi/camerafolder/pic.jpg",shell=True)
            print('PIC CAPTURED')
            time.sleep(0.2)
except KeyboardInterrupt:
    GPIO.cleanup()
