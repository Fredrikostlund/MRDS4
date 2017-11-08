#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Artificial Inteligence (kurskod)
Martin Sjölund
Fredrik Östlund
2017-09-25
"""

import http.client, json, time, sys
from math import sin,cos,tan,pi,atan2,sqrt,exp
from path import Path
from robot import *

SPEED = 0.7
LOOKAHEAD = 1

"""
Finds the first carrot coordinate
:param myPath: The stack containing the path coordinates
:param p: The position of the robot
:return: The carrot coordinate or a string
"""
def getCarrotCoordinate(myPath, p):
    i=0       
    while myPath:
        coordinate= myPath[i]
        
        d = calcDistance(p,coordinate)   
        
        if(d<LOOKAHEAD):
            myPath.pop(i)
        else:
            return coordinate
        i+=1
    return "No coordinate"

"""
Calculates the distance between two coordinates in a (x,y)-plane

:param p: First coordinate
:param c: Second coordinate
:return: The distance between the two coordinates
"""
def calcDistance(p,c):
    xc = c['X']
    yc = c['Y']
    xr = p['X']
    yr = p['Y']
    
    d = sqrt(((xc-xr)**2) + ((yc-yr)**2))    
    return d

"""
Calculates the angle between two coordinates

:param p: First coordinate
:param c: Second coordinate
:return: The angle between the coordinates
"""
def calcCoordinateAngle(p,c):
    xr = p['X']
    yr = p['Y']
    xc = c['X']
    yc = c['Y']
    
    angle = atan2((yc-yr),(xc-xr)) 
    return angle

"""
Calculates the heading angle of the robot

:param h: The heading coordinates
:return: The heading angle
"""
def calcHeadingAngle(h):
    return atan2(h['Y'], h['X'])

"""
Returns the robots position
:return: The robots position
"""
def getRobotPosition():
    return getPose()['Pose']['Position']

"""
Desides which path file to read
:return: The path file
"""
def main():
    if(len(sys.argv)>1):
        file_name=sys.argv[1]
    else:
        file_name='Path-to-bed.json'
    return file_name    


if __name__ == '__main__':
    
    file_name = main()
    path = Path()
    myPath = path.loadPath(file_name)
    
    try:
        while(myPath):
            p = getRobotPosition()
            h = getHeading()
            coordinate = getCarrotCoordinate(myPath, p)
            
            if coordinate != "no coordinate":
                
                coordinateAngle = calcCoordinateAngle(p,coordinate)
                headingAngle = calcHeadingAngle(h)
                
                turnAngle = coordinateAngle - headingAngle
                
                print(turnAngle)
                
                #optimizing turn distance
                if turnAngle > pi:
                    turnAngle = turnAngle - 2*pi
                elif turnAngle < -pi:
                    turnAngle = turnAngle + 2*pi 
                
                postSpeed(turnAngle, SPEED)
                
    except IndexError as ex:
        postSpeed(0,0)
        print("GOL GOL GOL!!")            
            
   