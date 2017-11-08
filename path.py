#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json

class Path:

    """
    Constructs a new 'Path' object.
    :return: returns nothing
    """
    def __init__(self):
    # Load the path from a file and convert it into a list of coordinates
        pass
     
    """
    Opens the json file and puts it in a stack
    :param file_name: The json file
    :return: The path stack
    """
    def loadPath(self, file_name):
    
        with open(file_name) as path_file:
            data = json.load(path_file)
            stack = []
            for i in range (len(data)):

                stack.append(data[i]['Pose']['Position'])
                
                stack.reverse
            return stack       
        
    def vectorizePath(self):
        vecArray = [{'X': p['Pose']['Position']['X'], \
                     'Y': p['Pose']['Position']['Y'], \
                     'Z': p['Pose']['Position']['Z']}\
                     for p in self.path]
        return vecArray
