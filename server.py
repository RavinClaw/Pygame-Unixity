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

server_address = ("localhost", 3115)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(server_address)
server.listen(1)
print("Server is running:", server_address)

player_positions = []


try:
    while True:
        conn, addr = server.accept()
        print("Connected to client:", addr)
        data_bytes = conn.recv(1024)
        data = pickle.loads(data_bytes)
        player_position = data["position"]
        player_positions.append(player_position)

        data = {"positions": player_positions}
        data_bytes = pickle.dumps(data)
        conn.sendall(data_bytes)
        conn.close()
except socket.error as e:
    print(e)
except KeyboardInterrupt:
    print("You stopped the server by using Ctrl+Z or Ctrl+C")
finally:
    server.close()
