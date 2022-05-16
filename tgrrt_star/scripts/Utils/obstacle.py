import numpy as np
import matplotlib.pyplot as plt

def check_obstacle(node,c, r = 10.5):
    x = node[0]
    y = node[1]
    flag1 = False
    flag2 = False
    flag3 = False
    flag4 = False

    # Circle with clearance of 5
    if((x-300)**2 + (y-160)**2 <= (15+c+r)**2):
        flag1 = True
    if((x-200)**2 + (y-80)**2 <= (15+c+r)**2):
        flag2 = True
    if((x-75)**2 + (y-175)**2 <= (15+c+r)**2):
        flag3 = True
        
    # padding of 5 on both x and y
    if(((x>=0) and (x<=c+r)) or ((x>=400-c-r) and (x<=400)) or ((y>=0) and (y<=c+r)) or ((y>=250-c-r) and (y<=250))):
        flag4 = True
    
    return (flag1 or flag2 or flag3 or flag4)

def create_obstacles():
    
    grid_points =[]
    obstacles=[]
    obstacles_clearance = []
    x= 400
    y = 250
    for i in range(x+1):
        for j in range(y+1):
            grid_points.append([i,j])
    # define the obstacle space
    for x,y in grid_points:
        # for the circle
        if((x-300)**2 + (y-160)**2 <= 225):
            obstacles.append([x,y])
        # Circle with clearance of 5
        if((x-300)**2 + (y-160)**2 <= 30.5**2):
            obstacles_clearance.append([x,y])
        
        # for the circle
        if((x-200)**2 + (y-80)**2 <= 225):
            obstacles.append([x,y])
        # Circle with clearance of 5
        if((x-200)**2 + (y-80)**2 <= 30.5**2):
            obstacles_clearance.append([x,y])
            
        # for the circle
        if((x-75)**2 + (y-175)**2 <= 225):
            obstacles.append([x,y])
        # Circle with clearance of 5
        if((x-75)**2 + (y-175)**2 <= 30.5**2):
            obstacles_clearance.append([x,y])
        # padding of 5 on both x and y
        if(((x>=0) and (x<=5+10.5)) or ((x>=395-10.5) and (x<=400))):
            obstacles_clearance.append([x,y])
        if(((y>=0) and (y<=5+10.5)) or ((y>=245-10.5) and (y<=250))):
            obstacles_clearance.append([x,y])

    o = np.array(obstacles)
    oc = np.array(obstacles_clearance)
    # code to plot the obstacle space 

    # plt.xlim(0, 400)
    # plt.ylim(0, 250)
    # plt.scatter(oc[:,0], oc[:,1], c = 'g', s= 1, label = 'clearance of 5')
    # plt.scatter(o[:,0], o[:,1], c = 'r', s =1, label = 'obstacles')
    # plt.title('Obstacle space')
    # plt.savefig('Obstacle_space.png')
    # plt.show()

    
    return obstacles, obstacles_clearance

