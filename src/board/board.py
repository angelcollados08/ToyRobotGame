from dataclasses import dataclass, field
from robot import Robot
from position import Position
from direction import Direction
from wall import Wall
from typing import Optional, Set

@dataclass
class Board():
    robot: Optional[Robot] = None
    size: int = 5
    walls: Set[Wall] = field(default_factory=set)

    def is_valid_move(self,pos: Position, dir: str) -> bool:
        valid_pos = pos.valid(self.size) and (Wall(pos) not in self.walls)
        valid_dir = True
        try:
            Direction[dir]
        except:
            valid_dir = False
        return valid_pos and valid_dir

    def place_robot(self, pos: Position, dir: Direction) -> None:
        pos.normalize_position()
        if self.is_valid_move(pos,dir):
            new_dir = Direction[dir]
            if self.robot is None:
                self.robot = Robot(pos,dir)
            self.robot.set_robot(pos,new_dir)

    def place_wall(self,pos: Position) -> None:
        pos.normalize_position()
        if pos.valid(self.size) and not ((self.robot and self.robot.position == pos) or (Wall(pos) in self.walls)):
            wall = Wall(pos)
            self.walls.add(wall)

    def report(self) -> None:
        if self.robot:
            print(self.robot.report())

    def left(self) -> None:
        if self.robot:
            self.robot.facing = self.robot.facing.turn("LEFT")

    def right(self) -> None:
        if self.robot:
            self.robot.facing = self.robot.facing.turn("RIGHT")



