# Recruitment Task


This project uses Q-learning to train an agent Harry Potter to reach the Cup in a maze, while escaping a Death Eater controlled by BFS.The environment is maze(15*10) with walls in between, and the cup, Harry the Death eater, all occupy individual cells in this grid this environment is rendered using Pygame.

---
-Objective
  - The maze is a 15x10 grid
  - Harry, the Cup, and a Death Eater spawn randomly in non-wall cells.
  - The Death Eater uses BFS (Breadth First Search) to chase Harry.
  - Harry learns using Q-learning to reach the Cup without getting caught.
---

## Basic Approach

| Component      | Description |
|----------------|-------------|
| **Algorithm**  | Q-learning with ε-greedy policy |
| **State**      | `(Harry_pos, Cup_pos, DeathEater_pos)` |
| **Actions**    | `[0: Up, 1: Down, 2: Left, 3: Right]` |
| **Rewards**    | +200 (reach Cup), -100 (caught), -1 (step), -10 (invalid move) |
| **Death Eater**| Moves 1 step toward Harry each turn using BFS, avoids Cup |

---
- Assumptions Made
  - Maze is defined in a text file with `'X'` as wall and `' '` as walkable space.
  - Harry, Cup, and Death Eater are all placed randomly on different free cells at the start of each episode.
  - The Cup is treated as a wall for the Death Eater.
  - Episodes end when Harry reaches the Cup or is caught by the Death Eater.
---
## File Structure

- environment.py
- qlearning.py
- main.py 
- run_trained.py 
- trained_q_table.pkl
- metrics.pkl
- README.md

---
## How to run 


