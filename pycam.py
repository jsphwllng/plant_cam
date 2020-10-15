import pygame
import pygame.camera
from pygame.locals import *
import time
import random
#start the webcam

def capture_plant():
    #initiates the webcam
    pygame.init()
    pygame.camera.init()
    if random.randint(0, 100) == 33:
        cam = pygame.camera.Camera("/dev/video2",(1080,1080), "YUV")
    elif random.randint(0,100) == 34:
        cam = pygame.camera.Camera("/dev/video2",(1080,1080), "HSV")
    else:
        cam = pygame.camera.Camera("/dev/video2",(1080,1080))
    cam.start()
    #sleep for one second to allow camera to focus, etc
    time.sleep(10)
    #open image and save
    image = cam.get_image()
    pygame.image.save(image, "image.jpg")
    #turn off webcam
    cam.stop()
    print("image saved!")
