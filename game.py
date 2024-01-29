import pygame
import random

GRID_SIZE = 4
CELL_SIZE = 100
GRID_MARGIN = 10
FONT_SIZE = 36
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]

pygame.init()

screen = pygame.display.set_mode((GRID_SIZE * CELL_SIZE + (GRID_SIZE + 1) * GRID_MARGIN,
                                  GRID_SIZE * CELL_SIZE + (GRID_SIZE + 1) * GRID_MARGIN))
pygame.display.set_caption('2048 Game')

font = pygame.font.Font(None, FONT_SIZE)

def add_tile():
    empty_cells = [(i, j) for i in range(GRID_SIZE) for j in range(GRID_SIZE) if grid[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        grid[i][j] = 2 if random.random() < 0.9 else 4

def draw_grid():
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            pygame.draw.rect(screen, GRAY, (j * (CELL_SIZE + GRID_MARGIN) + GRID_MARGIN,
                                            i * (CELL_SIZE + GRID_MARGIN) + GRID_MARGIN,
                                            CELL_SIZE, CELL_SIZE))

            value = grid[i][j]
            if value:
                color = (255, 255, 255)
                pygame.draw.rect(screen, color, (j * (CELL_SIZE + GRID_MARGIN) + GRID_MARGIN,
                                                i * (CELL_SIZE + GRID_MARGIN) + GRID_MARGIN,
                                                CELL_SIZE, CELL_SIZE))
                text = font.render(str(value), True, BLACK)
                text_rect = text.get_rect(center=(j * (CELL_SIZE + GRID_MARGIN) + GRID_MARGIN + CELL_SIZE // 2,
                                                  i * (CELL_SIZE + GRID_MARGIN) + GRID_MARGIN + CELL_SIZE // 2))
                screen.blit(text, text_rect)

def merge_tiles():
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE - 1):
            if grid[i][j] == grid[i][j + 1] and grid[i][j] != 0:
                grid[i][j] *= 2
                grid[i][j + 1] = 0

def move_left():
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE - 1):
            while grid[i][j] == 0 and any(grid[i][j + 1:]):
                for k in range(j, GRID_SIZE - 1):
                    grid[i][k] = grid[i][k + 1]
                grid[i][GRID_SIZE - 1] = 0

def move(direction):
    if direction == 'left':
        move_left()
        merge_tiles()
        move_left()
    elif direction == 'right':
        pass
    elif direction == 'up':
        pass
    elif direction == 'down':
        pass

def main():
    add_tile()
    add_tile()

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move('left')
                elif event.key == pygame.K_RIGHT:
                    pass
                elif event.key == pygame.K_UP:
                    pass
                elif event.key == pygame.K_DOWN:
                    pass

                add_tile()

        screen.fill(WHITE)
        draw_grid()
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
