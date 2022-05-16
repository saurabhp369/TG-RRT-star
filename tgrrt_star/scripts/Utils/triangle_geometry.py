import numpy as np
import math

def incenter(s, g , random):
    c = round(math.dist(s[:2], g[:2]))
    a = round(math.dist(random[:2], g[:2]))
    b = round(math.dist(s[:2], random[:2]))
    x1= s[0]
    x2 = g[0]
    x3 = random[0]
    y1= s[1]
    y2 = g[1]
    y3 = random[1]
    inc_x = (a * x1 + b * x2 + c * x3) / (a + b + c)
    inc_y = (a * y1 + b * y2 + c * y3) / (a + b + c)
    
    return [inc_x, inc_y]


def centroid(s, g, random):
    x1= s[0]
    x2 = g[0]
    x3 = random[0]
    y1= s[1]
    y2 = g[1]
    y3 = random[1]
    cen_x = (x1 + x2 + x3)/3
    cen_y = (y1 + y2 + y3)/3
    return [cen_x, cen_y]