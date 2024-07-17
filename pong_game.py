import pygame
import sys

pygame.init()

# Screen dimensions
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Paddle dimensions
paddle_width, paddle_height = 10, 100

# Ball properties
ball_radius, ball_speed = 7, [4, 4]

# Initial positions
left_paddle_pos = [10, height // 2 - paddle_height // 2]
right_paddle_pos = [width - 20, height // 2 - paddle_height // 2]
ball_pos = [width // 2, height // 2]
