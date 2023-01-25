import random
import copy

class AlphaBetaBoard():
    
    def __init__(self, board, previous_move = [None, None]):
        self.board = board
        self.turn = 2
        self.previous_move = previous_move

    def change_player(self):
        #FINISHED
        #switches the player of the board
        if self.turn == 1:
            self.turn = 2
        else:
            self.turn = 1

    def find_row_index(self, move):
        #FINISHED
        #returns the row index of the board for the move that will be played
        for row in range(len(self.board)):
            if self.board[row][move] != 0:
                return row - 1
        return len(self.board) - 1

    def is_terminal(self):
        #FINISHED
        #determines if the game is in a terminal state (does not account for a win terminal state)
        for col in range(len(self.board[0])):
            if self.board[0][col] == 0:
                return False
        return True

    def get_actions(self):
        #FINISHED
        #finds the available moves that can be played on the board
        actions = []
        for col in range(len(self.board[0])):
            if self.board[0][col] == 0:
                actions.append(col)
        return actions

    def successor(self):
        #FINISHED
        #finds a random successor state for a player 
        succ = copy.deepcopy(self)
        moves = succ.get_actions()
        if len(moves) != 0:
            move = random.choice(moves)
            row = succ.find_row_index(move)
            succ.board[row][move] = self.turn
            succ.change_player()
            succ.previous_move = [row, move]
        return succ

    def win(self):
        #NEEDS TESTING
        #determines the player who has won the game (if a win state has been reached), None if no player has won
        row = self.previous_move[0]
        col = self.previous_move[1]

        if row == None or col == None:
            return 0
        
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
                return -1
            if count_2 == 4:
                return 1
        
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
                return -1
            if count_2 == 4:
                return 1
        
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
                return -1
            if count_2 == 4:
                return 1
        
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
                return -1
            if count_2 == 4:
                return 1

        return 0

