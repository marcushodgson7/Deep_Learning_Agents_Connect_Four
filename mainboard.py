import random

class MainBoard:

    def __init__(self, previous_move = [None, None]):
        self.previous_move = previous_move
        self.board = self._new_board()
        self.turn = random.randint(1, 2)

    def find_row_of_move(self, move):
        #returns the row index of the board for the move that will be played
        if move > 6 or move < 0:
            return None
        for row in range(len(self.board)):
            if self.board[row][move] != 0:
                return row - 1
        return len(self.board) - 1

    def change_player(self):
        #changes the player
        if self.turn == 1:
            self.turn = 2
        else:
            self.turn = 1

    def _new_board(self):
        #return a new board of 0s
        return [[0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0]]

    def is_terminal(self):
        #determines if the game is in a terminal state (does not account for a win terminal state)
        for col in range(len(self.board[0])):
            if self.board[0][col] == 0:
                return False
        return True
    
    def win(self):
        #determines the player who has won the game (if a win state has been reached), None if no player has won
        row = self.previous_move[0]
        col = self.previous_move[1]

        if row == None or col == None:
            return None
        
        count_1, count_2 = 0, 0

        for change in range(-3, 4):
            c = col + change
            r = row
            if c < 0 or c > 6:
                continue
            if self.board[r][c] == 1:
                count_1 += 1
                count_2 = 0
            elif self.board[r][c] == 2:
                count_2 += 1
                count_1 = 0
            else:
                count_1, count_2 = 0, 0
            if count_1 == 4:
                return 1
            if count_2 == 4:
                return 2
        
        count_1, count_2 = 0, 0

        for change in range(-3, 4):
            r = row + change
            c = col
            if r < 0 or r > 5:
                continue
            if self.board[r][c] == 1:
                count_1 += 1
                count_2 = 0
            elif self.board[r][c] == 2:
                count_2 += 1
                count_1 = 0
            else:
                count_1, count_2 = 0, 0
            if count_1 == 4:
                return 1
            if count_2 == 4:
                return 2
        
        count_1, count_2 = 0, 0

        for change in range(-3, 4):
            r = row + change
            c = col + change
            if r < 0 or r > 5 or c < 0 or c > 6:
                continue
            if self.board[r][c] == 1:
                count_1 += 1
                count_2 = 0
            elif self.board[r][c] == 2:
                count_2 += 1
                count_1 = 0
            else:
                count_1, count_2 = 0, 0
            if count_1 == 4:
                return 1
            if count_2 == 4:
                return 2
        
        count_1, count_2 = 0, 0

        for change in range(-3, 4):
            r = row + change
            c = col - change
            if r < 0 or r > 5 or c < 0 or c > 6:
                continue
            if self.board[r][c] == 1:
                count_1 += 1
                count_2 = 0
            elif self.board[r][c] == 2:
                count_2 += 1
                count_1 = 0
            else:
                count_1, count_2 = 0, 0
            if count_1 == 4:
                return 1
            if count_2 == 4:
                return 2
        return None
