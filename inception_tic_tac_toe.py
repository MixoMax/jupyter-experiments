# Inception Tic Tac Toe
# A game of Tic Tac Toe where the board is made up of smaller Tic Tac Toe boards
# Each move in a small board determines which board the next player must play in

from typing import Union
from bidict import bidict

class Board:
    __board: list[list[Union[str, None, "Board"]]]
    
    def __init__(self) -> None:
        self.__board = [[None for _ in range(3)] for _ in range(3)]
    
    def get_value(self, x_cord: int, y_cord: int) -> Union[str, None, "Board"]:
        return self.__board[x_cord][y_cord]
    
    def set_value(self, x_cord: int, y_cord: int, value: str | None) -> None:
        self.__board[x_cord][y_cord] = value
    
    def clear(self) -> None:
        self.fill(None)
    
    def fill(self, value: str) -> None:
        self.__board = [[value for _ in range(3)] for _ in range(3)]
    
    def clear_numpad_numbers(self) -> None:
        #clear the numpad numbers from the board
        for x in range(3):
            for y in range(3):
                val = self.get_value(x, y)
                
                if str(val).isdigit():
                    self.set_value(x, y, None)
    
    def show_numpad_numbers(self) -> None:
        #set the fields of the board to the numpad numbers
        for x in range(3):
            for y in range(3):
                
                val = self.get_value(x, y)
                
                if val is None:
                    num = numpad_to_cords.inverse[(y, x)]
                    self.set_value(x, y, num)
    
    def won_by(self) -> None | str:
        #check if the board is won by a player
        #return the player if the board is won, else return None
        
        won_player = None
        
        triplets = []
        
        for y in range(3):
            triplets.append([(x, y) for x in range(3)])
        
        for x in range(3):
            triplets.append([(x, y) for y in range(3)])
        
        triplets.append([(x, x) for x in range(3)])
        triplets.append([(x, 2 - x) for x in range(3)])
        
        for triplet in triplets:
            values = [self.get_value(x, y) for x, y in triplet]
            
            if all([val == "X" for val in values]):
                won_player = "X"
                break
            elif all([val == "O" for val in values]):
                won_player = "O"
                break
        
        return won_player
    
    def total_won_by(self) -> None | str:
        #check each sub-board and check if the board is won by a player
        
        won_player = None
        
        triplets = []
        
        for y in range(3):
            triplets.append([(x, y) for x in range(3)])
        
        for x in range(3):
            triplets.append([(x, y) for y in range(3)])
        
        triplets.append([(x, x) for x in range(3)])
        triplets.append([(x, 2 - x) for x in range(3)])
        
        for triplet in triplets:
            values = [self.get_value(x, y).won_by() for x, y in triplet]
            
            if all([val == "X" for val in values]):
                won_player = "X"
                break
            
            elif all([val == "O" for val in values]):
                won_player = "O"
                break
        
        return won_player
    
    def __str__(self) -> str:
        out_str = ""
        
        for x in range(3):
            for y in range(3):
                val = self.get_value(x, y)
                
                if val is None:
                    out_str += " "
                else:
                    out_str += val.__str__()
                
                if y < 2:
                    out_str += "|"
            
            out_str += "\n"
            
            if x < 2:
                out_str += "-+-+-\n"
        
        return out_str
    
    def __repr__(self) -> str:
        #print board with boards as values
        out_str = ""
        
        #assume that each value is a board
        
        #   | | || | | || | |
        # -+-+- ||-+-+- ||-+-+-
        #   | | || | | || | |
        # -+-+- ||-+-+- ||-+-+-
        #   | | || | | || | |
        #
        # =================
        #
        # | |   || | | || | |
        # -+-+- ||-+-+- ||-+-+-
        #   | | || | | || | |
        # -+-+- ||-+-+- ||-+-+-
        #   | | || | | || | |
        #
        # =================
        #
        #   | | || | | || | |
        # -+-+- ||-+-+- ||-+-+-
        #   | | || | | || | |
        # -+-+- ||-+-+- ||-+-+-
        #   | | || | | || | |
        #
        
        #for each row
        #for each board in row
        #print the board, then print a space, then print the next board, then print a space, then print the next board
        
        out_str = ""
        for y in range(3):
            boards = [self.get_value(x, y) for x in range(3)]
            
            str_lists = [board.__str__().split("\n") for board in boards]
            
            for idx in range(len(str_lists[0]) - 1):
                out_str += " || ".join([str_list[idx] for str_list in str_lists]) + "\n"
            
            if y < 2:
                out_str += "=" * 24 + "\n"
                
                
        return out_str



# Main game loop

board = Board()

for x in range(3):
    for y in range(3):
        board.set_value(x, y, Board())

numpad_to_cords = { #numpad number -> (x, y)
    #indexing starts from the top left
    7: (0, 0),
    8: (1, 0),
    9: (2, 0),
    
    4: (0, 1),
    5: (1, 1),
    6: (2, 1),
    
    1: (0, 2),
    2: (1, 2),
    3: (2, 2)
}

numpad_to_cords = bidict(numpad_to_cords)
    

current_playing_board = board.get_value(1, 1) #start in the middle board
while True:
    current_playing_board.show_numpad_numbers()
    
    print(board.__repr__())
    
    print("Player 1, make your move")
    move = int(input())
    
    x_board, y_board = numpad_to_cords[move]
    
    current_playing_board.set_value(y_board, x_board, "X")
    
    current_playing_board.clear_numpad_numbers()
    
    won_player = current_playing_board.won_by()
    
    if won_player is not None:
        current_playing_board.fill(won_player)
    
    current_playing_board = board.get_value(x_board, y_board)
    
    won_player_total = board.total_won_by()
    print(won_player_total)
    if won_player_total is not None:
        print(f"Player {won_player_total} has won!")
        break
    
    #---
    
    current_playing_board.show_numpad_numbers()
    
    print(board.__repr__())
    
    print("Player 2, make your move")
    move = int(input())
    
    x_board, y_board = numpad_to_cords[move]
    
    current_playing_board.set_value(y_board, x_board, "O")
    current_playing_board.clear_numpad_numbers()
    
    
    won_player = current_playing_board.won_by()
    
    if won_player is not None:
        current_playing_board.fill(won_player)
    
    current_playing_board = board.get_value(x_board, y_board)
    
    won_player_total = board.total_won_by()
    print(won_player_total)
    if won_player_total is not None:
        print(f"Player {won_player_total} has won!")
        break
            
            