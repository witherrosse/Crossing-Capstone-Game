## Turtle Crossing Game - How it works

This is a **Turtle Crossing Game** (like Frogger) built with Python's Turtle module. You control a turtle trying to cross a busy road without getting hit by cars.

### Project files

- `player.py` – controls turtle movement
- `car_manager.py` – creates and moves cars
- `scoreboard.py` – tracks level and shows game over
- `main.py` – runs the main game loop

### What is used

- `turtle` module: for graphics and animation
- `time` module: to control game speed
- `random` module: for random car colors and timing

### How it works

1. Turtle starts at the bottom of the screen
2. Press **W** to move the turtle upward
3. Cars move from right to left at different speeds
4. Goal: reach the top finish line without hitting a car
5. Each time you reach the top:
   - Level increases by 1
   - Cars move faster
   - Turtle returns to starting position
6. Game ends if turtle hits any car

### Controls

| Key | Action |
|-----|--------|
| W | Move forward (up) |

### Game rules

- Each level makes cars faster
- Cars appear randomly (about 1 in 6 chance each frame)
- Different colored cars for variety
- Game over when collision happens

### Features

- Car speed increases each level
- Random car colors
- Smooth turtle movement
- Level display at top left

---

Help the turtle cross the road safely! Try to reach the highest level.
