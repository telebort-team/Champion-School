from picamera import PiCamera
from PIL import Image
from time import sleep

try:
    camera = PiCamera()
    camera.start_preview(fullscreen=False, window=(800,330,400,400))
    sleep(2)
    camera.capture('image.jpg')
    

except KeyboardInterrupt:
    print("User executed KeyboardInterrupt")
    print("Stopping python script...")

finally:
    camera.stop_preview()
    camera.close()
