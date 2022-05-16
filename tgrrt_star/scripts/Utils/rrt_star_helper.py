import random
import math
import numpy as np
import matplotlib.pyplot as plt
from Utils.obstacle import *

def random_sample(h,w):
    x = random.randint(16, w - 16)
    y = random.randint(16, h - 16)
    return [x,y]

def random_sample_cen(h,w):
    x = random.randint(int(-3*w), int(3*w))
    y = random.randint(int(-3*h), int(3*h))
    return [x,y]

def nearest(Vertices, new_x):
    min_dist = np.inf
    for i in Vertices:
        vertex = [i[0],i[1]]
        distance = round(math.dist(vertex, new_x),2)
        if distance < min_dist:
            min_dist = distance
            nearest_x = i
    return nearest_x  

def check_intersection(p1, p2):
    radius = 30.5
    center = [[300,160], [200, 80], [75, 175]]
    flag = None
    if check_obstacle(p1, 5) or check_obstacle(p2,5):
        return True
    for c in center:
        d = np.array(p2[:2]) - np.array(p1[:2])
        f = np.array(p1[:2]) - np.array(c)
        a = np.dot(d, d)
        b = 2 * np.dot(d, f)
        c = np.dot(f, f) - radius * radius
        dist = np.linalg.norm(d)
        discriminant = b * b - 4 * a * c
        flag = True
        if discriminant < 0:
            flag = False

        t1 = (-b + np.sqrt(discriminant)) / (2 * a);
        t2 = (-b - np.sqrt(discriminant)) / (2 * a);

        if (t1 < 0 and t2 < 0) or (t1 > 1 and t2 > 1):
            flag = False
        if flag:
            return True
    return flag

def take_action(cur_state,l, i):
    status = False
    x = cur_state[0] + l*math.cos(math.radians(cur_state[2]+(i*30)))
    y = cur_state[1] + l*math.sin(math.radians(cur_state[2]+(i*30)))
    if (y <= 250 and y>=0 and x>=0 and  x<= 400):
        new_node = [x, y, int(cur_state[2]+(i*30))]
        n = new_node.copy()

        if n[2]<0:
            n[2] = (360 + n[2])
        elif n[2]>360:
            n[2] = (n[2]-360)
        else:
            n[2] = n[2]
        status = True
    else:
        n  = [0,0,0]
    return status, n

def steer(x1, x2, l, k):
    min_dist = np.inf
    new_x = []
    for i in range(-k,k+1):
        status, node_state = take_action(list(x1), l, i)
        if status:
            if not check_intersection(node_state, x1):
                node = [node_state[0], node_state[1]]
                distance = round(math.dist(node, x2),2)
                if distance < min_dist:
                    min_dist = distance
                    new_x = node_state
                    new_x.append(distance + x1[-1])
    return new_x


def Near(Vertices, x, num_vertices):
    eta = 10
    d = 3 #no of dimensions
    gamma = 50
#     C = 1
    radius = min(gamma*math.pow((np.log(num_vertices))/(num_vertices), (1/d)), eta)
    neighbours = []
    for i in Vertices:
        node = [i[0], i[1]]
        distance = round(math.dist(node, x[:2]),2)
        if distance < radius:
            neighbours.append(i)
    return neighbours

def find_parent(E, x):
    for i in range(len(E)):
        if E[i][1] == x:
            return E[i][0], i
