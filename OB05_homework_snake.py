import pygame
import sys
import random

# Настройки
WINDOW_SIZE = 400
GRID_SIZE = 20
FPS = 4  # Змейка движется медленно!

# Цвета
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)
WHITE = (255, 255, 255)

def draw_block(screen, color, position):
    rect = pygame.Rect(position[0], position[1], GRID_SIZE, GRID_SIZE)
    pygame.draw.rect(screen, color, rect)

def random_position():
    x = random.randint(0, (WINDOW_SIZE - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
    y = random.randint(0, (WINDOW_SIZE - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
    return (x, y)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption('Змейка')
    clock = pygame.time.Clock()

    snake = [(100, 100), (80, 100), (60, 100)]
    direction = (GRID_SIZE, 0)
    apple = random_position()
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != (0, GRID_SIZE):
                    direction = (0, -GRID_SIZE)
                elif event.key == pygame.K_DOWN and direction != (0, -GRID_SIZE):
                    direction = (0, GRID_SIZE)
                elif event.key == pygame.K_LEFT and direction != (GRID_SIZE, 0):
                    direction = (-GRID_SIZE, 0)
                elif event.key == pygame.K_RIGHT and direction != (-GRID_SIZE, 0):
                    direction = (GRID_SIZE, 0)

        # Движение змейки
        new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
        if (new_head[0] < 0 or new_head[0] >= WINDOW_SIZE or
            new_head[1] < 0 or new_head[1] >= WINDOW_SIZE or
            new_head in snake):
            print(f'Игра окончена! Ваш счёт: {score}')
            pygame.quit()
            sys.exit()

        snake.insert(0, new_head)

        # Проверка на съедание яблока
        if new_head == apple:
            score += 1
            apple = random_position()
            while apple in snake:
                apple = random_position()
        else:
            snake.pop()

        # Отрисовка
        screen.fill(BLACK)
        draw_block(screen, RED, apple)
        for block in snake:
            draw_block(screen, GREEN, block)
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()