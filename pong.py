# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 22:58:56 2020

@author: 91942
"""


import pygame,sys
import random
pygame.init()
clock = pygame.time.Clock()
width = 1280
height = 760
screen = pygame.display.set_mode((width,height))

ball = pygame.Rect(width/2 - 15,height/2 - 15,20,20)
player = pygame.Rect(width - 20,height/2 - 70,10,140)
opponent = pygame.Rect(10, height/2 - 70,10,140)
color = pygame.Color('grey12')
light_grey = (200,200,200)
ball_speed_x = 7 
ball_speed_y = 7 
player_speed = 0
opponent_speed= 7
def ball_animation():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    if ball.top <= 0 or ball.bottom >= height:
      ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= width:
        ball_restart()
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1
def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= height:
        player.bottom = height
        
def opponent_animation():
    if opponent.top <  ball.y:
        opponent.top += opponent_speed
    if opponent.bottom >  ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= height:
        opponent.bottom = height
        
def ball_restart():
    global ball_speed_x,ball_speed_y
    ball.center = (width/2,height/2)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_speed += 7
            if event.key == pygame.K_DOWN:
                player_speed -= 7
    ball_animation()
    player_animation()
    opponent_animation()
        
    screen.fill(color)            
    pygame.draw.rect(screen, light_grey,player)
    pygame.draw.rect(screen,light_grey,opponent)
    pygame.draw.ellipse(screen,light_grey,ball)
    pygame.draw.aaline(screen,light_grey,(width/2,0),(width/2,height))
    pygame.display.flip()
    clock.tick(60)