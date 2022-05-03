from picamera import PiCamera
camera = PiCamera()
time.sleep(2)

camera.resolution = (1280, 720)

file_name = "/home/pi/Pictures/img_" + str(time.time()) + ".jpg"
camera.capture(file_name)
print("Done.")