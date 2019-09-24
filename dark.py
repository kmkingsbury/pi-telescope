from picamera import PiCamera
from time import sleep
from fractions import Fraction
import datetime
now = datetime.datetime.now()

print(now.year)

#camera = PiCamera()
# Force sensor mode 3 (the long exposure mode), set
# the framerate to 1/6fps, the shutter speed to 6s,
# and ISO to 800 (for maximum gain)
camera = PiCamera(
        resolution=(1280, 720),
        framerate=Fraction(1, 6),
        sensor_mode=3)
camera.shutter_speed = 6000000
camera.iso = 800
# Give the camera a good long time to set gains and
# measure AWB (you may wish to use fixed AWB instead)
for j in range(30):
    print("J:"+ str(j))
    sleep(1)

camera.exposure_mode = 'off'
for i in range(5):
    now = datetime.datetime.now()    
    print("now =", now)
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d-%m-%Y_%H.%M.%S")
    print("date and time =", dt_string)
    camera.capture('/home/pi/Desktop/darktestimage-%s.jpg' % dt_string)
    sleep(1)
# Finally, capture an image with a 6s exposure. Due
# to mode switching on the still port, this will take
# longer than 6 seconds

#camera.capture('dark.jpg')
