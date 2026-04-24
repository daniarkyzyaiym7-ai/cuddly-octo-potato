import pygame
import random
import sys

# -------------------- INIT --------------------
pygame.init()

WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game - Levels Edition")

clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 180, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# -------------------- SNAKE CLASS --------------------
class Snake:
    def __init__(self):
        self.body = [(100, 100), (80, 100), (60, 100)]
        self.direction = (CELL_SIZE, 0)
        self.grow = False

    def move(self):
        head_x, head_y = self.body[0]
        dx, dy = self.direction

        new_head = (head_x + dx, head_y + dy)
        self.body.insert(0, new_head)

        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

    def change_direction(self, dx, dy):
        # Prevent reversing directly
        if (dx, dy) == (-self.direction[0], -self.direction[1]):
            return
        self.direction = (dx, dy)

    def draw(self):
        for i, block in enumerate(self.body):
            color = GREEN if i == 0 else DARK_GREEN
            pygame.draw.rect(screen, color, (*block, CELL_SIZE, CELL_SIZE))

    def check_self_collision(self):
        return self.body[0] in self.body[1:]


# -------------------- FOOD --------------------
def generate_food(snake):
    while True:
        x = random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        y = random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE

        # Ensure food does not spawn on snake
        if (x, y) not in snake.body:
            return (x, y)


# -------------------- GAME --------------------
def game():
    snake = Snake()
    food = generate_food(snake)

    score = 0
    level = 1
    foods_to_next_level = 3

    speed = 8

    font = pygame.font.SysFont("Arial", 20)

    running = True
    while running:
        clock.tick(speed)

        # ---------------- EVENTS ----------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction(0, -CELL_SIZE)
                elif event.key == pygame.K_DOWN:
                    snake.change_direction(0, CELL_SIZE)
                elif event.key == pygame.K_LEFT:
                    snake.change_direction(-CELL_SIZE, 0)
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction(CELL_SIZE, 0)

        # ---------------- MOVE ----------------
        snake.move()

        head_x, head_y = snake.body[0]

        # ---------------- WALL COLLISION ----------------
        if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
            break

        # ---------------- SELF COLLISION ----------------
        if snake.check_self_collision():
            break

        # ---------------- FOOD COLLISION ----------------
        if snake.body[0] == food:
            snake.grow = True
            food = generate_food(snake)

            score += 1
            foods_to_next_level -= 1

            # Level up logic
            if foods_to_next_level == 0:
                level += 1
                foods_to_next_level = 3
                speed += 2   # increase speed each level

        # ---------------- DRAW ----------------
        screen.fill(BLACK)

        snake.draw()

        pygame.draw.rect(screen, RED, (*food, CELL_SIZE, CELL_SIZE))

        # UI: score & level
        text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
        screen.blit(text, (10, 10))

        pygame.display.update()

    # ---------------- GAME OVER SCREEN ----------------
    screen.fill(BLACK)
    game_over_text = font.render(f"Game Over! Score: {score}", True, WHITE)
    screen.blit(game_over_text, (WIDTH//2 - 100, HEIGHT//2))
    pygame.display.update()

    pygame.time.delay(2000)


# -------------------- RUN GAME --------------------
game()