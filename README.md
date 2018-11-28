# Autonomous Turtlebot3 

To make turtlebot wonder around freely, we are using the lidar mounted on it's top. 

Code mainly depends on a subscriber for /scan topic and a publisher for /cmd_vel topic.

## measurer(msg): (subscriber callback function)

This function is responsible from getting lidar scans from /scan topic and looking for 8 points in forward direction of the turtlebot. 

Looking at the points in 60 degrees in each direction with 20 degree intervals.
<img width="600" alt="Turtlebot3 Lidar Area Search" src="/imgs/turtle_bot_lidar_angles.jpg">

Adding point distances to path array for further use.
```python
	for counter, i in enumerate(range(0,60,20)):					
		paths.append([round(msg.ranges[int(i*360/float(len(msg.ranges)))],2),counter*15])
		paths.append([round(msg.ranges[int((360-i*15)/float(len(msg.ranges)))],2),-(counter*15)])
```

Searching for the max path and min path values for deciding the way to go.
```python
for path in paths:
		#print("path value: {} degree: {}".format(path[0],path[1]))
		if path[0] > max_value:
			max_value = path[0]
			degree = path[1]
		if path[0] < min_value:
			min_value = path[0]
```

Controlling if all the distance values in the sarch area more than SAFE_DISTANCE. If not, it means there is no where left to go. Turning turtlebot to it's back with a fast action. If there is a safe way to go, go to the point with max distance.
```python
if max_value < SAFE_DISTANCE:
		print("CAUTION")
		twist_message.linear.x = -0.8
		twist_message.angular.z = (2*math.pi)
else:
		twist_message.linear.x = 0.2
		twist_message.angular.z = (2*math.pi*degree/360)*1.25
```

### A short video of the turtlebot
<a href="https://www.youtube.com/watch?v=-6guHBeAUWA" target="_blank">Youtube Video: Turtlebot having a tour in the simulator.</a>

## Known errors and possible solutions

As it can be seen on the video sometimes turtlebot stucks at walls. That's happening because this version does not have a planner but sending Twist messages directly to the turtlebot. And sometimes turtlebot finds a safe way to go while hitting the wall (see at the end of the video where left side of the turtlebot is open). 

## More to add

Turtle bot can be provided SLAM to map the simulation zone so it will not only rely on lidar results but also past experiences.  





