def is_orientation_unique(piece_a, pieces):
    for piece in pieces:
        if not are_unique(piece_a, piece):
            return False
    return True

def are_unique(piece_a, piece_b):
    first_block = piece_a[0]
    for b_block in piece_b:
        potential_translation = (b_block[0] - first_block[0], b_block[1] - first_block[1])
        translated_a = [
            (block[0] + potential_translation[0], block[1] + potential_translation[1])
            for block in piece_a
        ]
        if set_equal(translated_a, piece_b):
            return False

    return True

def set_equal(set_a, set_b):
    if len(set_a) != len(set_b):
        return False
    for a in set_a:
        if a not in set_b:
            return False
    return True


class PuzzlePiece:
    def __init__(self):
        self.build_orientations()
    
    def flip(self):
        self.base = [(p[0], -p[1]) for p in self.base]
    
    def ccw_rotate(self):
        self.base = [(p[1], -p[0]) for p in self.base]
    
    def build_orientations(self):
        self.orientations = []
        for i in range(4):
            if is_orientation_unique(self.base, self.orientations):
                self.orientations.append(self.base)
            self.ccw_rotate()
        self.flip()
        for i in range(4):
            if is_orientation_unique(self.base, self.orientations):
                self.orientations.append(self.base)
            self.ccw_rotate()

class Block(PuzzlePiece):
    """
    X X X
    X X X
    """
    def __init__(self):
        self.base = [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2)]
        self.value = "block"
        super().__init__()

class LPiece(PuzzlePiece):
    """
    X
    X   
    X X X
    """
    def __init__(self):
        self.base = [(0,0), (0,1), (0,2), (1,0), (2,0)]
        self.value = "L"
        super().__init__()
        

class UPiece(PuzzlePiece):
    """
    X   X
    X X X
    """
    def __init__(self):
        self.base = [(0,0), (1,0), (1,1), (1,2), (0,2)]
        self.value = "U"
        super().__init__()
        

class LongLPiece(PuzzlePiece):
    """
    X
    X   
    X
    X X 
    """
    def __init__(self):
        self.base = [(0,0), (1,0), (2,0), (3,0), (3,1)]
        self.value = "longL"
        super().__init__()
        

class TPiece(PuzzlePiece):
    """
    X
    X   
    X X
    X 
    """
    def __init__(self):
        self.base = [(0,0), (1,0), (2,0), (3,0), (2,1)]
        self.value = "T"
        super().__init__()
        


class DPiece(PuzzlePiece):
    """
      X 
    X X
    X X
    """
    def __init__(self):
        self.base = [(0,0), (1,0), (2,0), (1,-1), (2,-1)]
        self.value = "d"
        super().__init__()
        

class StepPiece(PuzzlePiece):
    """
        X
    X X X
    X
    """
    def __init__(self):
        self.base = [(0,0), (0,1), (0,2), (-1,2), (1,0)]
        self.value = "step"
        super().__init__()

class WeirdStep(PuzzlePiece):
    """
    X X X
        X X
    """
    def __init__(self):
        self.base = [(0,0), (0,1), (0,2), (1,2), (1,3)]
        self.value = "weird"
        super().__init__()


block = Block()
l_piece = LPiece()
u_piece = UPiece()
long_l_piece = LongLPiece()
t_piece = TPiece()
d_piece = DPiece()
step_piece = StepPiece()
weird_step = WeirdStep()
        
