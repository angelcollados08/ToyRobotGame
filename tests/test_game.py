import pytest
import sys
import os
BASE_DIR = os.getcwd()
SRC_DIR = os.path.join(BASE_DIR,"src")
if SRC_DIR not in sys.path:
    sys.path.append(SRC_DIR)

from board import Board
from position import Position
from wall import Wall



def test_create_robot():
    board = Board()
    board.place_robot(Position(1,1),"NORTH")
    assert board.robot and board.robot.position.x == 0 and board.robot.position.y == 0 and board.robot.facing.name == "NORTH"

def test_create_robot_wrong_facing():
    board = Board()
    board.place_robot(Position(1,1),"NFERF")
    assert board.robot == None

def test_create_robot_wrong_position():
    board = Board()
    board.place_robot(Position(8,1),"NFERF")
    assert board.robot == None

def test_create_robot_with_wall():
    board = Board()
    board.place_wall(Position(2,2))
    board.place_robot(Position(2,2),"NORTH")
    assert  board.robot == None

def test_create_robot_twice():
    board = Board()
    board.place_robot(Position(2,2),"NORTH")
    board.place_robot(Position(1,1),"SOUTH")
    assert  board.robot and board.robot.position.x == 0 and board.robot.position.y == 0 and board.robot.facing.name == "SOUTH"

def test_create_wall():
    board = Board()
    wall_pos = Position(2,2)
    wall_pos.normalize_position()
    board.place_wall(Position(2,2))
    assert  Wall(wall_pos) in board.walls

def test_create_wall_wrong_position():
    board = Board()
    wall_pos = Position(8,2)
    wall_pos.normalize_position()
    board.place_wall(Position(8,2))
    assert not Wall(wall_pos) in board.walls

def test_create_wall_with_robot():
    board = Board()
    board.place_robot(Position(2,2),"NORTH")
    board.place_wall(Position(2,2))
    wall_pos = Position(2,2)
    wall_pos.normalize_position()
    assert  not Wall(wall_pos) in board.walls

def test_report(capsys):
    board = Board()
    board.place_robot(Position(1,1),"NORTH")
    board.report()
    printInformation = capsys.readouterr()
    assert "1,1,NORTH" in printInformation.out

def test_move_robot_north(capsys):
    board = Board()
    board.place_robot(Position(1,1),"NORTH")
    board.move()
    board.report()
    printInformation = capsys.readouterr()
    assert "1,2,NORTH" in printInformation.out

def test_move_robot_south(capsys):
    board = Board()
    board.place_robot(Position(1,2),"SOUTH")
    board.move()
    board.report()
    printInformation = capsys.readouterr()
    assert "1,1,SOUTH" in printInformation.out   

def test_move_robot_east(capsys):
    board = Board()
    board.place_robot(Position(2,2),"EAST")
    board.move()
    board.report()
    printInformation = capsys.readouterr()
    assert "3,2,EAST" in printInformation.out 

def test_move_robot_west(capsys):
    board = Board()
    board.place_robot(Position(2,2),"WEST")
    board.move()
    board.report()
    printInformation = capsys.readouterr()
    assert "1,2,WEST" in printInformation.out   

def test_move_robot_obstacle(capsys):
    board = Board()
    board.place_robot(Position(2,2),"WEST")
    board.place_wall(Position(1,2))
    board.move()
    board.report()
    printInformation = capsys.readouterr()
    assert "2,2,WEST" in printInformation.out  

def test_move_north_edge(capsys):
    board = Board()
    board.place_robot(Position(2,5),"NORTH")
    board.move()
    board.report()
    printInformation = capsys.readouterr()
    assert "2,1,NORTH" in printInformation.out

def test_move_robot_south_edge(capsys):
    board = Board()
    board.place_robot(Position(1,1),"SOUTH")
    board.move()
    board.report()
    printInformation = capsys.readouterr()
    assert "1,5,SOUTH" in printInformation.out 

def test_move_robot_east_edge(capsys):
    board = Board()
    board.place_robot(Position(5,2),"EAST")
    board.move()
    board.report()
    printInformation = capsys.readouterr()
    assert "1,2,EAST" in printInformation.out 

def test_move_robot_west_edge(capsys):
    board = Board()
    board.place_robot(Position(1,2),"WEST")
    board.move()
    board.report()
    printInformation = capsys.readouterr()
    assert "5,2,WEST" in printInformation.out 

def test_move_empty_robot():
    board = Board()
    board.move()
    assert board.robot == None

def test_robot_turn_left_north(capsys):
    board = Board()
    board.place_robot(Position(1,1),"NORTH")
    board.left()
    board.report()
    printInformation = capsys.readouterr()
    assert "1,1,WEST" in printInformation.out

def test_robot_turn_left_west(capsys):
    board = Board()
    board.place_robot(Position(1,1),"WEST")
    board.left()
    board.report()
    printInformation = capsys.readouterr()
    assert "1,1,SOUTH" in printInformation.out

def test_robot_turn_left_south(capsys):
    board = Board()
    board.place_robot(Position(1,1),"SOUTH")
    board.left()
    board.report()
    printInformation = capsys.readouterr()
    assert "1,1,EAST" in printInformation.out

def test_robot_turn_left_east(capsys):
    board = Board()
    board.place_robot(Position(1,1),"EAST")
    board.left()
    board.report()
    printInformation = capsys.readouterr()
    assert "1,1,NORTH" in printInformation.out

def test_robot_turn_right_north(capsys):
    board = Board()
    board.place_robot(Position(1,1),"NORTH")
    board.right()
    board.report()
    printInformation = capsys.readouterr()
    assert "1,1,EAST" in printInformation.out

def test_robot_turn_right_east(capsys):
    board = Board()
    board.place_robot(Position(1,1),"EAST")
    board.right()
    board.report()
    printInformation = capsys.readouterr()
    assert "1,1,SOUTH" in printInformation.out

def test_robot_turn_right_south(capsys):
    board = Board()
    board.place_robot(Position(1,1),"SOUTH")
    board.right()
    board.report()
    printInformation = capsys.readouterr()
    assert "1,1,WEST" in printInformation.out

def test_robot_turn_right_west(capsys):
    board = Board()
    board.place_robot(Position(1,1),"WEST")
    board.right()
    board.report()
    printInformation = capsys.readouterr()
    assert "1,1,NORTH" in printInformation.out

def test_data_first(capsys):
    board = Board()
    board.place_robot(Position(3,3),"NORTH")
    board.place_wall(Position(3,5))
    board.move()
    board.move()
    board.right()
    board.move()
    board.move()
    board.move()
    board.report()
    printInformation = capsys.readouterr()
    assert "1,4,EAST" in printInformation.out

def test_data_second(capsys):
    board = Board()
    board.place_robot(Position(2,2),"WEST")
    board.place_wall(Position(1,1))
    board.place_wall(Position(2,2))
    board.place_wall(Position(1,3))
    board.left()
    board.left()
    board.move()
    board.report()
    printInformation = capsys.readouterr()
    assert "3,2,EAST" in printInformation.out


    