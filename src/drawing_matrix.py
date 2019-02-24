"""
Copyright 2019, Aleksandar Stojimirovic <stojimirovic@yahoo.com>

Licence: MIT
Source: https://github.com/hooppler/pyHopfieldNeuralNetwork
"""

import pygame
from math import *


class DrawingMatrix(object):
    prev_pos = (0,0)
    def __init__(self, width=300, height=300, fields=(20,20), pos=(0,0), trashold=0):
        self.pos_x = pos[0]
        self.pos_y = pos[1]
        self.width = width
        self.height = height
        self.max_diameter = min([self.width, self.height])
        self.fields_x = fields[0]
        self.fields_y = fields[1]
        self.max_fields = max([self.fields_x, self.fields_y])
        self.d = int(round(float(self.max_diameter)/float(self.max_fields)))
        self.dx = int(floor(self.width/self.fields_x))
        self.dy = int(floor(self.height/self.fields_y))
        self.trashold = trashold

        self.surface = pygame.Surface((self.fields_x*self.dx+1, self.fields_y*self.dy+1))
        #self.surface.set_alpha(100)
        
        
        self.fields = []
        for x in range(0, self.fields_x):
            for y in range(0, self.fields_y):
                self.fields.append(0)
                
        #                          R    G    B
        self.BLACK = pygame.Color( 0 ,  0 ,  0 )
        self.WHITE = pygame.Color(255, 255, 255)
        self.COLOR1 = pygame.Color(255,255,180)
        self.COLOR2 = pygame.Color(88,88,88)
        
        self.update()
                
    
    def draw_matrix(self):
        for x in range(0, self.fields_x):
            for y in range(0, self.fields_y):
                if self.fields[y*self.fields_x + x] <= self.trashold:
                    pygame.draw.rect(self.surface, self.COLOR1, (x*self.dx, y*self.dy, self.dx, self.dy))
                else:
                    pygame.draw.rect(self.surface, self.COLOR2, (x*self.dx, y*self.dy, self.dx, self.dy))
        #pygame.draw.rect(canvas, COLOR, (100, 200, 10, 10))
        for x in range(0, self.fields_x+1):
            pygame.draw.line(self.surface, self.BLACK, (x*self.dx, 0), (x*self.dx, self.fields_y*self.dy))
        for y in range(0, self.fields_y+1):
            pygame.draw.line(self.surface, self.BLACK, (0, y*self.dy), (self.fields_x*self.dx, y*self.dy))
    
    
    def is_coordinate_in_button(self, pos):
        pass
    
    
    def update(self, events=None):
        
        left, middle, right = pygame.mouse.get_pressed()
        if events is not None:
            if left:
                m_x, m_y = pygame.mouse.get_pos()
                m_x = m_x - self.pos_x
                m_y = m_y - self.pos_y
                #print("x={} y={}".format(m_x, m_y))
                s_x = int(floor(m_x/self.dx))
                s_y = int(floor(m_y/self.dy))
                
                if not (s_x, s_y) == self.prev_pos:
                    if ((s_x<self.fields_x and s_y<self.fields_y) and (s_x>=0 and s_y>=0)):
                        if self.fields[s_y * self.fields_x + s_x] == 1:
                            self.fields[s_y * self.fields_x + s_x] = 0
                        else:
                            self.fields[s_y * self.fields_x + s_x] = 1
                self.prev_pos = (s_x, s_y)
        
        self.draw_matrix()
        
    
    def get_surface(self):
        return self.surface
    
    
    def get_pattern(self):
        return self.fields
        
    def set_pattern(self, pattern):
        self.fields = pattern
        
    def clear(self):
        for x in range(0, self.fields_x):
            for y in range(0, self.fields_y):
                self.fields[y*self.fields_x+x] = 0
    
    
    def get_position(self):
        return (self.pos_x, self.pos_y)
        
        
    def get_fields_xy(self):
        return (self.fields_x, self.fields_y)