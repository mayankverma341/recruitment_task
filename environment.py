import pygame
import random
import numpy as np
from collections import deque

cell_size = 32
maze_width = 15
maze_height = 10
wall = 'X'
empty_space = ' '

class maze:
    def __init__(self, mazefile):
        self.maze = self.load_maze(mazefile)
        self.freecells = [(x, y) for y in range(maze_height) for x in range(maze_width) if self.maze[y][x] == empty_space]
        self.reset()

    def reset(self):
        self.harry = random.choice(self.freecells)
        self.cup = random.choice([cell for cell in self.freecells if cell != self.harry])
        self.deatheater = random.choice([cell for cell in self.freecells if cell != self.harry and cell != self.cup])

        self.done = False
        return self.get_state()

    def load_maze(self,filename):
        with open(filename, 'r') as file:
            lines = file.read().splitlines()
        List = []
        for line in lines:
            List.append(list(line))
        return List

    def is_valid(self, pos, check_cup=True):
        x, y = pos
        if 0 <= x < maze_width and 0 <= y < maze_height:
            if self.maze[y][x] == empty_space:
                if check_cup and pos == self.cup:
                    return False
                return True
        return False

    def get_state(self):
        return (self.harry, self.cup, self.deatheater)

    def step(self, action):
        reward = -1
        new_pos = self.move(self.harry, action, check_cup=False)
        if new_pos == self.harry:
            reward -= 10  # hitting a wall (invalid move)
        self.harry = new_pos
        self.deatheater = self.bfs(self.deatheater, self.harry)
        if self.harry == self.deatheater:
            reward -= 100
            self.done = True
        elif self.harry == self.cup:
            reward += 200
            self.done = True
        return self.get_state(), reward, self.done

    def move(self, pos, action, check_cup=True):
        x, y = pos
        if action == 0:
            y -= 1
        elif action == 1:
            y += 1
        elif action == 2:
            x -= 1
        elif action == 3:
            x += 1
        new_pos = (x, y)
        return new_pos if self.is_valid(new_pos, check_cup=check_cup) else pos



    def bfs(self, start, goal):
        visited = set()
        queue = deque([(start, [])])
        while queue:
            (current, path) = queue.popleft()
            if current == goal:
                return path[0] if path else current
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ny, nx  = current[1] + dy, current[0] + dx
                next_pos = (nx, ny)
                if self.is_valid(next_pos, check_cup=True) and next_pos not in visited:
                    visited.add(next_pos)
                    queue.append((next_pos, path + [next_pos]))
        return start













