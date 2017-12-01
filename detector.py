
from gpiozero import DistanceSensor, LED, MotionSensor,Robot
import gpiozero
from signal import pause
import time
pir = MotionSensor(12)
sensor = DistanceSensor(21, 20, max_distance=1, threshold_distance=0.2)
led = LED(16)
robot = Robot(left=(26, 19), right=(6, 13))

def sense():
    #stop robot
    robot.stop()
    #record time
    start = time.time()
    #this function will stop when it see's any motion but if will stop anyway after 2 seconds
    pir.wait_for_motion(timeout=2)
    #if it took less than 2 seconds for the waitForMotion fuction to stop then it detected movement
    if time.time() - start < 1.9999999:
        #buzzer on
        led.on()
        #wait 2 seconds
        time.sleep(2)
        #buzzer off
        led.off()
    else:
        #the thing in front of the robot is a walll
        #turn to get out of the way
        robot.left()
        time.sleep(1)
        robot.stop()
    
            
def move():
    robot.forward()

sensor.when_in_range = sense
when_out_of_range = move

pause()
