from board import Board
from pieces import (
    block,
    l_piece,
    u_piece,
    long_l_piece,
    t_piece,
    d_piece,
    step_piece,
    weird_step    
)

class PlacedPiece:
    def __init__(self, piece, start_point, o_idx):
        self.piece = piece
        self.start_point = start_point
        self.o_idx = o_idx

def solve(month, day, placed_piecs, unplaced_pieces):
    b = Board()
    b.set_date(month, day)
    for p in placed_piecs:
        b.add_piece(p.piece, p.start_point, p.o_idx)
    
    if len(unplaced_pieces) == 0:
        b.print_board()
        return True
    
    unplaced_piece = unplaced_pieces[0]
    for open_space in b.open_spaces():
        for o_idx in range(len(unplaced_piece.orientations)):
            if b.add_piece(unplaced_piece, open_space, o_idx):
                if solve(month, day, placed_piecs + [PlacedPiece(unplaced_piece, open_space, o_idx)], unplaced_pieces[1:]):
                    return True
                b.remove_piece(unplaced_piece, open_space, o_idx)
    return False

solve(
    month=4,
    day=12,
    placed_piecs=[],
    unplaced_pieces=[block, l_piece, u_piece, long_l_piece, t_piece, 
                     d_piece, step_piece, weird_step]
)
