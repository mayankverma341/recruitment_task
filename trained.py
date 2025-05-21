import pygame
import time
from environment import maze
from qlearning import Agent

cell_size = 40
fps = 5
window_width = 15 * cell_size
window_height = 10 * cell_size


colors = {
    'wall': (40, 40, 40),'empty': (255, 255, 255),'harry': (0, 255, 0),'cup': (255, 215, 0),'death_eater': (255, 0, 0)}

def draw_grid(screen, maze, harry, cup, death_eater):
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            cell_type = maze[y][x]
            rect = pygame.Rect(x * cell_size, y*cell_size, cell_size, cell_size)
            if (x, y) == harry:
                color = colors['harry']
            elif (x, y) == cup:
                color = colors['cup']
            elif (x, y) == death_eater:
                color = colors['death_eater']
            elif cell_type == 'X':
                color = colors['wall']
            else:
                color = colors['empty']
            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, (0, 0, 0), rect, 1)  # border

def main():
    pygame.init()
    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Trained Agent")
    clock = pygame.time.Clock()

    env = maze('C:/Users/nv909/Downloads/V1.txt')

    agent = Agent(actions=[0, 1, 2, 3])
    agent.load('trained_q_table.pkl')

    running = True
    while running:
        state = env.reset()
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    done = True
                    break

            action = agent.choose_action(state)
            next_state, reward, done = env.step(action)
            state = next_state
            screen.fill((0, 0, 0))
            draw_grid(screen, env.maze, *state)
            pygame.display.flip()
            clock.tick(fps)

        time.sleep(1)

    pygame.quit()

if __name__ == "__main__":
    main()
