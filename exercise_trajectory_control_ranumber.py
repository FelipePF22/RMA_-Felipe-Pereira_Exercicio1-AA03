#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
 
# Time in ROS
def time():
   return rospy.get_rostime().secs + (rospy.get_rostime().nsecs/1e9)
 
# Stop robot
def stop():
   pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
   t = Twist()
   t.linear.x = 0
   t.linear.y = 0
   t.linear.z = 0
   t.angular.x = 0
   t.angular.y = 0
   t.angular.z = 0
   pub.publish(t)

# move robot front or back
def move_front_or_back(X: float, status: str):
   pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
   if status == 'back':
       X = X * -1
   else:
       X = X
   t = Twist()
   t.linear.x = X
   t.linear.y = 0
   t.linear.z = 0
   t.angular.x = 0
   t.angular.y = 0
   t.angular.z = 0
   pub.publish(t)

#rotation robot
def rottation (X: float):
   pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
   t = Twist()
   t.linear.x = 0
   t.linear.y = 0
   t.linear.z = 0
   t.angular.x = 0
   t.angular.y = 0
   t.angular.z = X
   pub.publish(t)

# Move robot
def move():
   # Topic to move
   rospy.init_node('movement_robot', anonymous=True)
   rospy.sleep(1)
   # Initialize counter
   tempo = time()
   # Will send message until stop the code
   while not rospy.is_shutdown():
       temp = time() - tempo
       # Move forward for 3 seconds at 1 m/s.
       if temp <= 3:
           move_front_or_back(1, 'front')
        # Stop for 1 second.
       elif temp > 3 and temp <= 4:
           stop()
       # Rotate counterclockwise for 2 seconds at 1 rad/s.
       elif temp > 4 and temp <=6:
           rottation(1)
        # Stop for 1 second.
       elif temp > 6 and temp <= 7:
           stop()
        # Move backward for 3 seconds at -0.5 m/s.
       elif temp > 7 and temp <= 10: 
          move_front_or_back(0.5, 'back')
        # Stop again for 1 second.
       elif temp > 10 and temp <= 11:
           stop()
        # restart the cicle
       #else:
        #  tempo = time()   
 
if __name__ == '__main__':
   try:
       move()
   except rospy.ROSInterruptException:
       pass

