#import modules
from gpiozero import Robot
from time import sleep
from picamera import PiCamera
from time import sleep
#start camera recording
camera = PiCamera()
camera.start_recording('video.h264')
#set up robot
robot = Robot(left=(26, 19), right=(6, 13))

#to control the robot we have used pygame
#this means that you dont have to press enter after every key you press(as with normal input in python)
#to do this he created a fake pygame window
import os

os.environ['SDL_VIDEODRIVER'] = 'dummy'
import pygame
pygame.init()
pygame.display.set_mode((1,1))

while 1:
    #this line waits for you to press somthing on the computer
    events = pygame.event.get()
    for e in events:
        print e
        #print e.key
        #if the key is the down arrow:
        if e.type == 2:
            print e.key
            if  e.key == 273:
                robot.backward()
            #if key is the up arrow
            elif e.key == 274:
                robot.forward()
            #right:
            elif e.key == 276:
                robot.right()
            #left:
            elif e.key == 275:
                robot.left()
            #space bar
            elif e.key == 32:
                robot.stop()
                
        pass
