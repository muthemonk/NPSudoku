# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 14:28:38 2016

@author: muthemonk
This is the NP Sudoku module for python 3.5
Generates a consistent n block board with n^2 blocks and cells
The nBoard class creates an instance of a n^2 board and will create a
logical layout based on the least common factors that = n
ie for a traditional 3^2 board it will create a 3 by 3 block and 
and 3 by 3 board of said blocks
"""
#import functools
import tkinter as tk

#def factors(n):  
#    f = []    
#    s = set(functools.reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
#    for i in s:
#        f.append(i)
#    f.sort()
#        
#    return f
 
#Block class made up of cells
class nblock:
    def __init__(self, coordinate, n):
        self.name = str(coordinate) + "block"
        self.blockaddress = coordinate
        self.cells = []
        for i in range(n**2):
            self.cells.append(cell(i))
    
#Base class that defines cell structures
class cell:
    def __init__(self, coordinate):
        self.name = "cell" + str(coordinate)       
        self.bcoordinate = coordinate
        self.number = None
        #self.dimensions = (3px, 3px)
        
    
    def UpdateCell(self, number):
        self.number = number
        
    def Value(self):
        return print("This cell contains the number " + str(self.number))
    
#Board generator for developing n^2 board        
class board:
    def __init__(self, n):
        self.name = "Size " + str(n**2) + " board"
        #generate a board consisting of nblocks with corresponding cells        
        self.blocks = []
        for i in range(n**2):
            self.blocks.append(nblock(i, n))
            

    
        
        