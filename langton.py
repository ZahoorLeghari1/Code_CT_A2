import pygame
import sys

# Constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
ANT_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]  # Colors for different ants

# Directions: 0 = up, 1 = right, 2 = down, 3 = left
directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]


class LangtonsAnt:
    def __init__(self, grid_size, start_x, start_y, color, wrap_around=False):
        self.grid_size = grid_size
        self.ant_x = start_x
        self.ant_y = start_y
        self.ant_direction = 0  # Start facing up
        self.color = color
        self.wrap_around = wrap_around

    def step(self, grid):
        # Change the color of the current cell
        if grid[self.ant_y][self.ant_x] == WHITE:
            grid[self.ant_y][self.ant_x] = BLACK
            self.ant_direction = (self.ant_direction + 1) % 4  # Turn right
        else:
            grid[self.ant_y][self.ant_x] = WHITE
            self.ant_direction = (self.ant_direction - 1) % 4  # Turn left

        # Move the ant forward
        self.ant_x += directions[self.ant_direction][0]
        self.ant_y += directions[self.ant_direction][1]

        # Handle boundary conditions
        if self.wrap_around:
            self.ant_x %= self.grid_size
            self.ant_y %= self.grid_size
        else:
            if not (0 <= self.ant_x < self.grid_size and 0 <= self.ant_y < self.grid_size):
                return False  # Ant moves out of bounds
        return True

    def draw(self, screen, cell_size):
        # Draw the ant
        pygame.draw.rect(screen, self.color, (self.ant_x * cell_size, self.ant_y * cell_size, cell_size, cell_size))


def run_simulation(grid_size=100, cell_size=5, speed=10, wrap_around=False, num_ants=2):
    pygame.init()
    screen_size = grid_size * cell_size
    screen = pygame.display.set_mode((screen_size, screen_size))
    clock = pygame.time.Clock()

    grid = [[WHITE for _ in range(grid_size)] for _ in range(grid_size)]

    # Create multiple ants with random starting positions and different colors
    ants = []
    for i in range(num_ants):
        start_x = grid_size // 2 + i  # Offset the ants slightly
        start_y = grid_size // 2
        color = ANT_COLORS[i % len(ANT_COLORS)]  # Cycle through available colors
        ants.append(LangtonsAnt(grid_size, start_x, start_y, color, wrap_around=wrap_around))
    # for i in range(num_ants):
    #     start_x = grid_size // 2  # All ants start at the center
    #     start_y = grid_size // 2
    #     color = ANT_COLORS[i % len(ANT_COLORS)]  # Cycle through available colors
    #     ants.append(LangtonsAnt(grid_size, start_x, start_y, color, wrap_around=wrap_around))


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Take one step for each ant
        for ant in ants:
            if not ant.step(grid):
                pygame.quit()
                sys.exit()

        # Draw the grid
        screen.fill(WHITE)
        for y in range(grid_size):
            for x in range(grid_size):
                color = grid[y][x]
                pygame.draw.rect(screen, color, (x * cell_size, y * cell_size, cell_size, cell_size))

        # Draw all ants
        for ant in ants:
            ant.draw(screen, cell_size)

        pygame.display.flip()
        clock.tick(speed)


if __name__ == "__main__":
    # Customize the grid size, speed, wrap-around behavior, and number of ants here
    run_simulation(grid_size=140, cell_size=5, speed=2000, wrap_around=True, num_ants=2)
