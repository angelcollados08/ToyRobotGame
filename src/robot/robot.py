from dataclasses import dataclass
from position import Position
from direction import Direction

@dataclass
class Robot():
    position: Position
    facing: Direction

    def set_robot(self,pos: Position, dir: Direction) -> None:
        self.position = pos
        self.facing = dir

    def report(self) -> str:
        return f"{self.position.x +1},{self.position.y + 1},{self.facing.name}"

