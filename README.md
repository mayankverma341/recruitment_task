# Recruitment Task


This project uses Q-learning to train an agent Harry Potter to reach the Cup in a maze, while escaping a Death Eater controlled by BFS.The environment is maze(15*10) with walls in between, and the cup, Harry the Death eater, all occupy individual cells in this grid this environment is rendered using Pygame.

---
## Objective
  - The maze is a 15x10 grid
  - Harry, the Cup, and a Death Eater spawn randomly in non-wall cells.
  - The Death Eater uses BFS (Breadth First Search) to chase Harry.
  - Harry learns using Q-learning to reach the Cup without getting caught.
---

## Basic Approach

| Component      | Description |
|----------------|-------------|
| **Algorithm**  | Q-learning with epsilon greedy policy |
| **State**      | `(Harry_pos, Cup_pos, DeathEater_pos)` |
| **Actions**    | `[0: Up, 1: Down, 2: Left, 3: Right]` |
| **Rewards**    | +200 (reach Cup), -100 (caught), -1 (step), -10 (invalid move) |
| **Death Eater**| Moves 1 step toward Harry each turn using BFS, avoids Cup |

---
## Assumptions Made
  - Maze is defined in a text file with `'X'` as wall and `' '` as walkable space.
  - Harry, Cup, and Death Eater are all placed randomly on different free cells at the start of each episode.
  - The Cup is treated as a wall for the Death Eater.
  - Episodes end when Harry reaches the Cup or is caught by the Death Eater.
---
## File Structure

- environment.py
- qlearning.py
- main.py 
- trained.py 
- trained_q_table.pkl
- metrics.pkl
- README.md

---
## How to run 

### For training the Agent

1. Save all project files (main.py, environment.py, q_learning.py, etc.) in a single folder.
2. Download the `V1.txt` maze file and save it into the same folder.
3. Copy the full file path of `V1.txt`:
4. Edit file paths in two files:
- In `main.py`, line **6**:
  ```python
  env = maze("C:/your/path/to/V1.txt")
  ```
- In `trained.py`, line **39**:
  ```python
  env = maze("C:/your/path/to/V1.txt")
  ```
5. Train the agent by running `main.py` file

### To run the trained Agent

After training is complete (or if you already have trained_q_table.pkl)
- Run the `trained.py` file to launch the game

### To view the training performance 
- Run `plot.py`

### Rendering details

- Each grid cell is 40x40 pixels.
- Entity colors:
  - Wall	       Black (40, 40, 40)
  - Empty Cell   Gray (230, 230, 230)
  - Harry     	 Green (0, 255, 0)
  - Cup	         Gold (255, 215, 0)
  - Death Eater	 Red (255, 0, 0)
- Maze is drawn using the provided text file eg `V1.txt`.


