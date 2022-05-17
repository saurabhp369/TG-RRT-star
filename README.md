**Requirements:**

    Python >= 3.8

    cv2 (OpenCV 4.5.5)

    numpy

    math

    random

    matplotlib

    rospy

    actionlib

    MoveBase

    warnings


Normal CV2 Visualization Instructions:

    1) Run as python3 tg_rrt_star.py
    2) Give the start and goal (x,y,theta) coordinates when prompted.
    3) Give step size as 5 for good visualization. Give no. of steps of 30 as 2, i.e., (-60, -30, 0, 30, 60) is actionset.
    4) Choose the algorithm you want to run
    5) Wait for algorithm to finish. (C-RRT* may take a while at times but rest should run quite fast).


ROS/Gazebo Instructions:

      1) Copy the contents of the provided package into the catkin workspace.

      2) catkin_make or catkin build and source devel/setup.bash

      3) You will need ros-noetic-navigation. (Installation by sudo apt-get install ros-noetic-navigation)

      4) For start and goal location of (150, 50, 0) --> (375, 225, 0)
      export Turtlebot3 Burger
      roslaunch tgrrt_star turtlebot.launch x_pos:=1.5 y_pos:=4.5 z_pos:=0
      roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=$HOME/catkin_ws/src/tgrrt_star/map/map.yaml
      In catkin_ws/src/tgrrt_star/scripts, run python3 tgrrt_star.py

      5) Basically start x and start y multiplied by 3/100 should give you the coordinates x_pos and y_pos to be entered in the roslaunch tgrrt_star  turtlebot.launch arguments.

Results:

RRT*


<img src="https://github.com/saurabhp369/TG-RRT-star/blob/main/visualisation/2_rrt.png">


TG-RRT* (Incenter based)

<img src="https://github.com/saurabhp369/TG-RRT-star/blob/main/visualisation/2_ic.png">



It can be concluded from the results that TG-RRT* explores lesser area and also takes lesser time and number of iterations to find an optimal path.
