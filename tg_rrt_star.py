#!/usr/bin/env python
import numpy as np
import math
import cv2
from Utils.triangle_geometry import *
from Utils.rrt_star_helper import *
import warnings
warnings.filterwarnings("ignore")

def RRT_star(h, w, start, goal, l, k, out, b, choice):
    selection = ['RRT_star', 'IC_RRT_star', 'C_RRT_star']
    print('********** Starting {} algorithm **********'.format(selection[choice-1]))
    start.append(0)
    V = [start]
    E = []
    i = 0
    while(True):
        
        if choice == 1:
            x = random_sample(h,w)
            if (check_obstacle(x,5)):
                continue
            x_gc = x
            use_geometry = False
        elif choice == 2:
            x = random_sample(h,w)
            if (check_obstacle(x,5)):
                continue
            x_gc = incenter(start, goal, x)
            use_geometry = check_obstacle(x_gc, 5)
        else:
            x = random_sample_cen(h,w)
            x_gc = centroid(start, goal, x)
            use_geometry = check_obstacle(x_gc, 5)
        
        if (not use_geometry):            
            x_nearest = nearest(V, x_gc)
            x_new = steer(x_nearest, x_gc, l, k)
            if (len(x_new) == 0):
                continue
            V.append(x_new)
            x_min = x_nearest
            X_near = Near(V, x_new, len(V))
            for x_neighbour in X_near:
                if not check_intersection(x_neighbour, x_new):
                    c_dash = x_neighbour[-1] + round(math.dist(x_neighbour[:2], x_new[:2]),2)
                    if c_dash < x_new[-1]:
                        x_min = x_neighbour
            E.append([x_min, x_new])
            cv2.line(b, (int(x_min[0]), int(250 - x_min[1])), (int(x_new[0]), int(250-x_new[1])),(255,0,255), 1 )
            out.write(b)
            for x_near in X_near:
                if (x_near != x_min):
                    if (not check_intersection(x_new, x_near) and x_near[-1] > x_new[-1] + round(math.dist(x_near[:2], x_new[:2]),2)):
                        x_parent, index = find_parent(E,x_near)
                        cv2.line(b, (int(x_parent[0]), int(250 - x_parent[1])), (int(x_near[0]), int(250-x_near[1])),(255,255,255), 1)
                        E.pop(index)
                        E.append([x_new, x_near])
                        cv2.line(b, (int(x_new[0]), int(250 - x_new[1])), (int(x_near[0]), int(250-x_near[1])),(255,0,255), 1)
                        out.write(b)
            if (round(math.dist(x_new[:2], goal[:2]),2) < 10):
                print('GOAL REACHED')
                print('Number of iterations completed:', i)
                break
            i+=1
        else:
            continue
    
    return V, E, out, b


def main():
    selection = ['RRT_star', 'IC_RRT_star', 'C_RRT_star']
    s_x = int(input('Enter the x-coordinate of start'))
    s_y = int(input('Enter the y-coordinate of start'))
    s_theta = int(input('Enter the theta of start'))
    g_x = int(input('Enter the x-coordinate of goal'))
    g_y = int(input('Enter the y-coordinate of goal'))
    g_theta = int(input('Enter the theta of goal'))
    l = int(input('Enter the step size'))
    k = int(input('Enter the number of steps of 30 in each direction'))
    ch = int(input('Enter the choice of algorithm 1: RRT*  2:Incenter-TGRRT* 3:Centroid TGRRT*'))
    start = [int(s_x),int(s_y), int(s_theta)]
    goal = [int(g_x), int(g_y), int(g_theta)]
    print(start)
    print(goal)
    background = np.zeros((251,401,3),np.uint8) 
    background.fill(255)
    frameSize = (400, 250)
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    out = cv2.VideoWriter('visualisation_{}.mp4'.format(selection[ch-1]),fourcc, 25, frameSize)
    obstacles, obstacles_clearance = create_obstacles()
    for c in obstacles:
        x = c[0]
        y = c[1]
        background[(250-y,x)]=[0,0,255] #assigning a red colour for the obstacles
    out.write(background)
    V, E, out, background = RRT_star(250, 400, start, goal, l, k, out, background, ch)
    path_list = []
    path_list.append(goal)
    goal_parent, _ = find_parent(E, V[-1])
    child = goal_parent
    rechd_start = False
    while True:
        parent, index = find_parent(E, child)
        path_list.append(parent)
        if(parent[:3] == start[:3]):
            break
        child = parent
    
    for i in range(len(path_list)-1):
        x1 = path_list[i][0]
        y1 = 250 - path_list[i][1]
        x2 = path_list[i+1][0]
        y2 = 250 - path_list[i+1][1]
        cv2.line(background, (int(x1), int(y1)), (int(x2), int(y2)) , (0,0,0), 1 )
    for i in range(int(100)):
        out.write(background)
    out.release()
    V = np.array(V)
    path = np.array(path_list)
    path = np.flip(path)
    print('The total cost is ', V[-1][-1]/100)
    print('Visualisation video created')


if __name__== '__main__':
    main()
