UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

GRID_SIZE = 50

import pygame
import random

screen = pygame.display.set_mode((750, 750))
clock = pygame.time.Clock()
running = True

corners = []
snake_length = 0
snake_pos = (0, 0)
snake = [[snake_pos, RIGHT]]
apple_pos = (random.randint(0, (750 / GRID_SIZE) - 1) * GRID_SIZE, random.randint(0, (750 / GRID_SIZE) - 1) * GRID_SIZE)
health = 3

start_time = pygame.time.get_ticks()
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake[0][1] = UP
            elif event.key == pygame.K_DOWN:
                snake[0][1] = DOWN
            elif event.key == pygame.K_LEFT:
                snake[0][1] = LEFT
            elif event.key == pygame.K_RIGHT:
                snake[0][1] = RIGHT
            corners.append([(snake[0][0][0], snake[0][0][1]), snake[0][1]])

    while snake_length + 1 > len(snake):
        if snake[-1][1] == UP:
            snake.append([(snake[-1][0][0], snake[-1][0][1] + 50), UP])
        elif snake[-1][1] == DOWN:
            snake.append([(snake[-1][0][0], snake[-1][0][1] - 50), DOWN])
        elif snake[-1][1] == LEFT:
            snake.append([(snake[-1][0][0] + 50, snake[-1][0][1]), LEFT])
        elif snake[-1][1] == RIGHT:
            snake.append([(snake[-1][0][0] - 50, snake[-1][0][1]), RIGHT])

    if snake[0][0][0] == apple_pos[0] and snake[0][0][1] == apple_pos[1]:
        snake_length += 1
        apple_pos = (random.randint(0, (750 / GRID_SIZE) - 1) * GRID_SIZE, random.randint(0, (750 / GRID_SIZE) - 1) * GRID_SIZE)

    for corner in corners:
        for i in range(len(snake)):
            s = snake[i]
            if s[0][0] == corner[0][0] and s[0][1] == corner[0][1] and i > 0:
                s[1] = corner[1]
            if s[0][0] == corner[0][0] and s[0][1] == corner[0][1] and i == len(snake) - 1:
                corners.remove(corner)
            elif s[0][0] == corner[0][0] and s[0][1] == corner[0][1] and i == 0:
                corner = [(s[0][0], s[0][1]), s[1]]

    for i in range(len(snake)):
        if i > 0 and snake[i][0][0] == snake[0][0][0] and snake[i][0][1] == snake[0][0][1]:
            health -= 1
            break
    if health < 1:
        print("You lost!")
        running = False

    if (pygame.time.get_ticks() - start_time) > 100:
        for i in range(len(snake)):
            s = snake[i]

            if s[1] == UP:
                s[0] = (s[0][0], s[0][1] - 50)
            elif s[1] == DOWN:
                s[0] = (s[0][0], s[0][1] + 50)
            elif s[1] == LEFT:
                s[0] = (s[0][0] - 50, s[0][1])
            elif s[1] == RIGHT:
                s[0] = (s[0][0] + 50, s[0][1])

        start_time = pygame.time.get_ticks()

    for i in snake:
        pygame.draw.rect(screen, (0, 255, 0), (i[0][0], i[0][1], GRID_SIZE, GRID_SIZE))

    pygame.draw.rect(screen, (255, 0, 0), (apple_pos[0], apple_pos[1], GRID_SIZE, GRID_SIZE))

    pygame.display.flip()
    clock.tick(60)