from dataclasses import dataclass

@dataclass
class Position():
    x:int
    y:int

    def normalize_position(self) -> None:
        self.x -=1
        self.y -=1

    def valid(self,board_size: int) -> bool:
        return 0 <= self.x < board_size and 0 <= self.y < board_size
    
    def __hash__(self):
        return hash((self.x, self.y))
    