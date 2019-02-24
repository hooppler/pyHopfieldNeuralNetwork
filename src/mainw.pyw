"""
Copyright 2019, Aleksandar Stojimirovic <stojimirovic@yahoo.com>

Licence: MIT
Source: https://github.com/hooppler/pyHopfieldNeuralNetwork
"""

import pygame
from pygame.locals import *
import sys
from drawing_matrix import DrawingMatrix
from button import Button
from hopfield_neural_network import HopfieldNeuralNetwork

# HopfieldNeuralNetwork Initialization
nn = HopfieldNeuralNetwork(100)
nn.set_random_w_tetha()
nn.set_random_input()


# Initialization
pygame.init()
pygame.font.init()
ArielFont = pygame.font.SysFont('Ariel', 30)
clock = pygame.time.Clock()

# Set display and main surface
surface = pygame.display.set_mode((500, 500))
surface.fill(pygame.Color(250, 250, 250))

# Draw on surfaces (main and others)
title = ArielFont.render('HopfieldNeuralNetwork Workbanch', True, pygame.Color(10,10,10))
pygame.draw.line(surface, pygame.Color(100,100,255), (60, 50), (415, 50), 1)
matrix = DrawingMatrix(fields=(10,10), pos=(90,100))
button_clear = Button(pos=(145, 420), title='Clear')
button_start_stop = Button(pos=(255, 420), title='Start/Stop')

matrix.set_pattern(nn.get_input())
matrix.update()

# Blit everything on main surface to become visible
surface.blit(title, (65, 30))
surface.blit(matrix.get_surface(), matrix.get_position())
surface.blit(button_clear.get_surface(), button_clear.get_position())
surface.blit(button_start_stop.get_surface(), button_start_stop.get_position())

# Update display
pygame.display.update()
            
flag_run = False
while True:
    clock.tick(60)
    
    left, middle, right = pygame.mouse.get_pressed()
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
        matrix.update(events=events)
        button_clear.update(events=events)
        button_start_stop.update(events=events)
        
        if button_clear.get_state() == 1:
            matrix.clear()
            pattern = matrix.get_pattern()
            input = []
            for i in range(0, len(pattern)):
                if pattern[i] > matrix.trashold:
                    input.append(1)
                else:
                    input.append(-1)
            nn.set_input(input)
            nn.range_init()
            nn.calculate()
            nn.clear_input()
            
        if button_start_stop.get_state() == 1:
            if flag_run:
                flag_run = False
            else:
                flag_run = True
                pattern = matrix.get_pattern()
                input = []
                for x in range(0, matrix.fields_x):
                    for y in range(0, matrix.fields_y):
                        if pattern[x * matrix.fields_y + y] > matrix.trashold:
                            input.append(1)
                        else:
                            input.append(-1)
                nn.set_input(input)
                nn.range_init()
                nn.calculate()
                nn.clear_input()
        
        surface.blit(matrix.get_surface(), matrix.get_position())
        surface.blit(button_clear.get_surface(), button_clear.get_position())
        surface.blit(button_start_stop.get_surface(), button_start_stop.get_position())
        
        pygame.display.update()

    if flag_run:
        nn.range_init()
        nn.calculate()
        matrix.set_pattern(nn.get_output())
        matrix.update()
        surface.blit(matrix.get_surface(), matrix.get_position())
        pygame.display.update()











