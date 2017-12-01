# pioneers-entry
Our entry to the 'only you can save us' pioneers competition.
The program called robot control allows us to control the robot 
To do this we first logged in to the raspberry pi through VNC.
Then we just had to run the program to control the robot.
As the VNC app is available on phone and PC we can control the robot from both.

The second program is an auto control program.
It makes the robot go forward until it senses something within a certain distance.
then it stops and see's if it can detect any motion.
If it can then it assumes it is a zombie.
Otherwise the thing in front of it is a wall.
If so, the robot turns about 45 degrees and starts again.
