"""
Copyright 2019, Aleksandar Stojimirovic <stojimirovic@yahoo.com>

Licence: MIT
Source: https://github.com/hooppler/pyHopfieldNeuralNetwork
"""

import pygame


class Button(object):
    def __init__(self, width=100, height=25, pos=(0,0), title='Button'):
        self.width = width
        self.height = height
        self.pos_x = pos[0]
        self.pos_y = pos[1]
        self.title = title
        self.font_size = 15
        self.state = 0
        
        self.color_pressed =        pygame.Color(130,130,74)
        self.color_not_pressed =    pygame.Color(195,192,105)
        self.color_border =         pygame.Color(150,150,150)
        
        self.surface = pygame.Surface((width, height))
        
        # Text Initialization
        pygame.font.init()
        font = pygame.font.SysFont('Arial', self.font_size)
        self.text_surface = font.render(title, True, (50,50,50))
        
        self.update()
        
        
    def draw_button(self, color):
        pygame.draw.rect(self.surface, color, (0, 0, self.width, self.height))
        pygame.draw.rect(self.surface, pygame.Color(150,150,150), (2, 2, self.width-4, self.height-4),1)
        
        
    def update(self, events=None):
    
        left_pressed, midle_pressed, right_pressed = pygame.mouse.get_pressed()
        self.state = 0
        
        if events == None:
            self.draw_button(self.color_not_pressed)
        
        else:
            for event in events:
                if left_pressed:
                    pos_x, pos_y = pygame.mouse.get_pos()
                    pos_x = pos_x - self.pos_x
                    pos_y = pos_y - self.pos_y
                    if (pos_x > 0 and pos_x < self.width) and (pos_y > 0 and pos_y < self.height):
                        self.state = 1
                        self.draw_button(self.color_pressed)

                    else:
                        self.draw_button(self.color_not_pressed)
        
                else:
                    self.draw_button(self.color_not_pressed)
                    
        self.surface.blit(self.text_surface, ((self.width-(self.font_size/2)*len(self.title))/2, (self.height-self.font_size)/2-2))
    
    def get_surface(self):
        return self.surface
        
        
    def get_state(self):
        return self.state
        
        
    def get_position(self):
        return (self.pos_x, self.pos_y)
        
