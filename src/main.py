from board import Board
from position import Position

def main():
    game_on = True
    board = Board()
    while game_on:
        input_user = input().split()
        if len(input_user) == 1:
            if input_user[0] == "MOVE":
                board.move()
            elif input_user[0] == "REPORT": 
                board.report()
            elif input_user[0] == "LEFT": 
                board.left()
            elif input_user[0] == "RIGHT": 
                board.right()
        elif len(input_user) == 2:
            parameters = input_user[1].split(',')
            if input_user[0] == "PLACE_WALL":
                if len(parameters) == 2 and parameters[0].isdigit() and parameters[1].isdigit():
                    board.place_wall(Position(int(parameters[0]),int(parameters[1])))
            elif input_user[0] == "PLACE_ROBOT":
                if len(parameters) == 3 and parameters[0].isdigit() and parameters[1].isdigit():
                    board.place_robot(Position(int(parameters[0]),int(parameters[1])),parameters[2])


if __name__ == "__main__":
    main()