class Board:
    def __init__(self):
        self.months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        self._reset_board()
    
    def _reset_board(self):
        self.pieces = []
        self.occupied = {}
        self.value = {}
        self.NUM_COLS = 7
        self.NUM_ROWS = 7

        for row in range(2):
            for col in range(self.NUM_COLS):
                if col < 6:
                    self.occupied[(row, col)] = False
                    self.value[(row, col)] = self.months[row*6 + col]
                else:
                    self.occupied[(row, col)] = True
                    self.value[(row, col)] = ""
        for row in range(2,6):
            for col in range(self.NUM_COLS):
                self.occupied[(row, col)] = False
                self.value[(row, col)] = (row-2)*self.NUM_COLS + col + 1
        for col in range(self.NUM_COLS):
            if col < 3:
                self.occupied[(6, col)] = False
                self.value[(6, col)] = 28 + col + 1
            else:
                self.occupied[(6, col)] = True
                self.value[(6, col)] = ""


    def print_board(self):
        for row_idx in range(self.NUM_ROWS):
            row = []
            for col_idx in range(self.NUM_COLS):
                value = self.value[(row_idx, col_idx)]
                row.append(f"{value:^5}")
            print('|'.join(row))
    
    def set_date(self, month, day):
        if month < 1 or month > 12:
            raise ValueError("Invalid month")
        if day < 1 or day > 31:
            raise ValueError("Invalid day")
        
        self._reset_board()
        month_row = (month - 1) // 6
        month_col = month % 6 - 1
        self.occupied[(month_row, month_col)] = True

        day_row = (day - 1) // self.NUM_COLS + 2
        day_col = day % self.NUM_COLS - 1
        self.occupied[(day_row, day_col)] = True
    
    def open_spaces(self):
        open_spaces = []
        for row_idx in range(self.NUM_ROWS):
            for col_idx in range(self.NUM_COLS):
                if not self.occupied[(row_idx, col_idx)]:
                    open_spaces.append((row_idx, col_idx))
        return open_spaces
    
    def add_piece(self, piece, start_point, o_idx):
        start_row, start_col = start_point
        orientation = piece.orientations[o_idx]

        for block in orientation:
            current_block = (start_row + block[0], start_col + block[1])
            if current_block not in self.occupied:
                return False
            if self.occupied[current_block]:
                return False
        
        for block in orientation:
            current_block = (start_row + block[0], start_col + block[1])
            self.occupied[current_block] = True
            self.value[current_block] = piece.value
        self.pieces.append((piece, start_point, o_idx))
        return True
    
    def remove_piece(self, piece, start_point, o_idx):
        start_row, start_col = start_point
        orientation = piece.orientations[o_idx]
        for block in orientation:
            current_block = (start_row + block[0], start_col + block[1])
            self.occupied[current_block] = False
            if current_block[0] < 2:
                month_idx = current_block[0] * 6 + current_block[1]
                self.value[current_block] = self.months[month_idx]
            elif current_block[0] < 6:
                day_value = (current_block[0] - 2) * self.NUM_COLS + current_block[1] + 1
                self.value[current_block] = day_value
            else:
                self.value[current_block] = 28 + current_block[1] + 1
        self.pieces.remove((piece, start_point, o_idx))