'''Snake Game'''

import pygame
import random
import sys

# Initiation
pygame.init()

# Game_Size
WIDTH = 500
HEIGHT = 500
CELL_SIZE = 20
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE
FPS = 10

# Color Management
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Game_Display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Snake Game")
clock = pygame.time.Clock()

# Snake, Food and Direction
snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
direction = (1, 0)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = (0, -1)
            elif event.key == pygame.K_DOWN:
                direction = (0, 1)
            elif event.key == pygame.K_LEFT:
                direction = (-1, 0)
            elif event.key == pygame.K_RIGHT:
                direction = (1, 0)

    # Updating Snake
    snake_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    snake.insert(0, snake_head) # type: ignore

    # When snake eats Food
    if snake_head == food:
        food = (random.randint(0, GRID_WIDTH - 1),
                random.randint(0, GRID_HEIGHT - 1))
    else:
        snake.pop()

    # Collision with walls
    if snake_head[0] < 0 or snake_head[0] >= GRID_WIDTH or snake_head[1] < 0 or snake_head[1] >= GRID_HEIGHT:
        running = False

    # Collision with body
    for segment in snake[1:]:
        if snake_head == segment:
            running = False

    # Game_Scene
    screen.fill(WHITE)
    for segment in snake:
        pygame.draw.rect(screen, GREEN, pygame.Rect(
            segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, RED, pygame.Rect(
        food[0] * CELL_SIZE, food[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.display.flip()
    clock.tick(FPS)

# Function to print "The End" when the game ends
if running == False:
    print("The End")

# Call the print_the_end function when the game ends
pygame.quit()
sys.exit()
