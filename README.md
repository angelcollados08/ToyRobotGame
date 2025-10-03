# ToyRobotGame
This repository contains a simple game to move a robot in a 5x5 board, the robot can move to north, south, east or west and you can find some walls in the path.

## Supported commands:
  - **PLACE_ROBOT ROW,COL,FACING**: This command places a robot at a given coordinate with an initial Facing direction.
        • If there are no robots on the board, the PLACE_ROBOT places one at the coordinate specified.
        • If there is already a robot, a new PLACE_ROBOT command moves the existing robot to the new
        location.
        • If the coordinate or facing value is invalid, then the game ignores it and does nothing.
    Accepted Facing values are: NORTH, SOUTH, EAST, WEST
  - **PLACE_WALL ROW,COL**: This command places a wall at the given coordinate.
        • If the target location is empty, then it adds a wall to it.
        • The user can add as many walls as they like until the board is filled.
        • If the target location is occupied (by the robot, or another wall), then this command is ignored.
        • Invalid coordinates are ignored.
  - **MOVE**: The MOVE command moves the robot 1 space forward in the direction it is currently facing.
        • If there are no robots on the board, this command is ignored.
        • If there is a wall in front of the robot, this command is ignored.
        • If the robot has already reached the edge of the board, a MOVE command towards the edge warps the robot to the opposite side of the board.
  - **LEFT / RIGHT**: Turns the robot 90 degrees to its current left or right.
  - **REPORT**: The game prints out the current location and facing direction of the robot.

## Requirements:
- Python **3.8+**
- Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

## Installation:
Clone the repository and navigate into the project folder:
```bash
git clone https://github.com/angelcollados08/ToyRobotGame.git
cd ToyRobotGame
```

## Usage:
Run the main program:
```bash
python main.py
```

Example:
```text
PLACE_ROBOT 1,1,NORTH
MOVE
PLACE_WALL 2,2
RIGHT
MOVE
REPORT
```

Expected output:
```text
2,1,EAST
```

## Running Tests:
Unit tests are included. Run them with:
```bash
pytest tests/
```

## Contributing:
1. Fork the repository  
2. Create your feature branch (`git checkout -b feature/new-feature`)  
3. Commit your changes (`git commit -m "Added new feature"`)  
4. Push to the branch (`git push origin feature/new-feature`)  
5. Open a Pull Request  