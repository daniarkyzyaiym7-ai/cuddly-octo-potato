import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MS Paint Style App")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

palette = [BLACK, RED, GREEN, BLUE, YELLOW]

current_color = BLACK
current_tool = "brush"  # brush, eraser, rect, circle
brush_size = 5
eraser_size = 20

screen.fill(WHITE)
canvas = screen.copy()

# Undo stack
history = []

drawing = False
start_pos = (0, 0)
prev_pos = None


def save_state():
    if len(history) > 20:
        history.pop(0)
    history.append(canvas.copy())


def draw_palette():
    for i, color in enumerate(palette):
        pygame.draw.rect(screen, color, (10 + i * 40, 10, 30, 30))


def restore():
    global canvas
    if history:
        canvas = history.pop()


running = True
while running:
    clock.tick(120)
    screen.blit(canvas, (0, 0))
    draw_palette()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_u:  # undo
                restore()

            if event.key == pygame.K_b:
                current_tool = "brush"
            if event.key == pygame.K_e:
                current_tool = "eraser"
            if event.key == pygame.K_r:
                current_tool = "rect"
            if event.key == pygame.K_c:
                current_tool = "circle"

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            # palette
            for i, color in enumerate(palette):
                rect = pygame.Rect(10 + i * 40, 10, 30, 30)
                if rect.collidepoint(x, y):
                    current_color = color

            save_state()
            drawing = True
            start_pos = event.pos
            prev_pos = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
            if current_tool == "rect":
                pygame.draw.rect(canvas, current_color, pygame.Rect(
                    min(start_pos[0], event.pos[0]),
                    min(start_pos[1], event.pos[1]),
                    abs(start_pos[0] - event.pos[0]),
                    abs(start_pos[1] - event.pos[1])
                ), 2)

            if current_tool == "circle":
                radius = int(((event.pos[0]-start_pos[0])**2 + (event.pos[1]-start_pos[1])**2) ** 0.5)
                pygame.draw.circle(canvas, current_color, start_pos, radius, 2)

            drawing = False
            prev_pos = None

    # BRUSH
    if drawing and current_tool == "brush":
        mouse = pygame.mouse.get_pos()
        pygame.draw.line(canvas, current_color, prev_pos, mouse, brush_size)
        prev_pos = mouse

    # ERASER
    if drawing and current_tool == "eraser":
        mouse = pygame.mouse.get_pos()
        pygame.draw.circle(canvas, WHITE, mouse, eraser_size)

    pygame.display.flip()

pygame.quit()
sys.exit()
