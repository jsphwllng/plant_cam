import pygame
import pygame.camera
from pygame.locals import *
import time

#start the webcam

def capture_plant():
    pygame.init()
    pygame.camera.init()
    cam = pygame.camera.Camera("/dev/video0",(640,640))
    cam.start()
    #sleep for one second to allow camera to focus, etc
    time.sleep(4)
    #open image and save

    image = cam.get_image()
    pygame.image.save(image, "image.jpg")

    print("image saved!")