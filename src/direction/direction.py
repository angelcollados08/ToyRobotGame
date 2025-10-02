from enum import Enum

class Direction(Enum):
    NORTH = (0,1)
    EAST = (1,0)
    SOUTH = (0,-1)
    WEST = (-1,0)

    def turn(self,turn:str):
        directions = list(Direction)
        if turn == "LEFT":
            new_dir = (directions.index(self)-1) % len(directions)
        elif turn == "RIGHT":
            new_dir = (directions.index(self) + 1) % len(directions)
        return directions[new_dir]