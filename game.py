import os
import sys
import random
import string
import asyncio
import socket
import selectors
import select
import getpass
import pygame
from pygame.locals import *
import math
import pickle


width = 500
height = 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("A Pygame Multiplayer Game")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ("localhost", 3115)
client.connect(server_address)

running = True
while running:
    player_position = pygame.mouse.get_pos()
    
    data = {"position": player_position}
    data_bytes = pickle.dumps(data)
    client.sendall(data_bytes)

    data_bytes = client.recv(1024)
    data = pickle.loads(data_bytes)
    player_positions = data["positions"]

    screen.fill((255,255,255))
    for position in player_positions:
        pygame.draw.rect(screen, (255,0,0), (position[0], position[1], 10, 10))
    pygame.draw.circle(screen, (0, 0, 255), player_position, 10, 10)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

client.close()
pygame.quit()