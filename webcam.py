import pygame
import pygame.camera
from pygame.locals import *
import time

pygame.init()
pygame.camera.init()

def capture_plant():
    pygame.init()
    pygame.camera.init()
    cam = pygame.camera.Camera("/dev/video2",(1080,1080))
    cam.start()
    #sleep for one second to allow camera to focus, etc
    time.sleep(4)
    #open image and save

    image = cam.get_image()
    pygame.image.save(image, "image.jpg")
    cam.stop()
    print("image saved!")

print(pygame.camera.list_cameras())
capture_plant()