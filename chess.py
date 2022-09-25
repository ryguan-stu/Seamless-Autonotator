import typing

class Piece: 
    row_mapping = {
        0: 'A',
        1: 'B',
        2: 'C',
        3: 'D',
        4: 'E',
        5: 'F',
        6: 'G',
        7: 'H',
    }
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def get_location():
        return f"{row_mapping[self.col]}{self.row}"
    

class Pawn(Piece):
    ...

class Knight(Piece):
    ...
        
class Queen(Piece):
    ...

class King(Piece):
    ...

