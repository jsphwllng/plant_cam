import pygame
import pygame.camera
from pygame.locals import *

#start the webcam
pygame.init()
pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0",(640,480))
cam.start()
#open image and save
image = cam.get_image()
pygame.image.save(image, "image.jpg")

print("image saved!")