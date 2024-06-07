import pygame
import random

# Ініціалізація Pygame
pygame.init()

# Параметри вікна
width = 800
height = 600
cell_size = 20
fps = 10

# Кольори
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

# Створення вікна гри
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Функція відображення тексту на екрані
def display_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    window.blit(text_surface, text_rect)

# Функція відображення змійки
def display_snake(snake):
    for segment in snake:
        pygame.draw.rect(window, green, (segment[0], segment[1], cell_size, cell_size))

# Функція генерації нової їжі
def generate_food(snake):
    food = [random.randrange(0, width - cell_size, cell_size),
            random.randrange(0, height - cell_size, cell_size)]
    while food in snake:
        food = [random.randrange(0, width - cell_size, cell_size),
                random.randrange(0, height - cell_size, cell_size)]
    return food

# Головна функція гри
def game():
    snake = [[width // 2, height // 2]]
    food = generate_food(snake)
    direction = "RIGHT"
    score = 0

    clock = pygame.time.Clock()

    # Головний цикл гри
    running = True
    while running:
        window.fill(black)

        # Обробка подій
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != "DOWN":
                    direction = "UP"
                elif event.key == pygame.K_DOWN and direction != "UP":
                    direction = "DOWN"
                elif event.key == pygame.K_LEFT and direction != "RIGHT":
                    direction = "LEFT"
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    direction = "RIGHT"

        # Рух змійки
        head = list(snake[0])
        if direction == "UP":
            head[1] -= cell_size
        elif direction == "DOWN":
            head[1] += cell_size
        elif direction == "LEFT":
            head[0] -= cell_size
        elif direction == "RIGHT":
            head[0] += cell_size
        snake.insert(0, head)

        # Перевірка на зіткнення з краєм екрану або самою собою
        if (head[0] < 0 or head[0] >= width or
            head[1] < 0 or head[1] >= height or
            head in snake[1:]):
            running = False

        # Перевірка, чи змійка з'їла їжу
        if head == food:
            score += 1
            food = generate_food(snake)
        else:
            snake.pop()

        # Відображення змійки та їжі
        display_snake(snake)
        pygame.draw.rect(window, red, (food[0], food[1], cell_size, cell_size))

        # Відображення рахунку
        display_text("Score: " + str(score), pygame.font.Font(None, 36), white, width // 2, 20)

        # Оновлення екрану
        pygame.display.update()

        # Затримка, щоб не перевищити fps
        clock.tick(fps)

    # Виведення повідомлення про кінець гри
    display_text("Game Over!", pygame.font.Font(None, 72), white, width // 2, height // 2)
    pygame.display.update()
    pygame.time.delay(2000)

# Запуск гри
game()

# Завершення Pygame
pygame.quit()
