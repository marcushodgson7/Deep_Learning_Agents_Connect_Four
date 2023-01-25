from alphabetaboard import AlphaBetaBoard
import copy


def minimax(board, depth, alpha, beta, player):
    if board.win() == 1:
        return (None, 10000000)
    elif board.win() == -1:
        return (None, -10000000)
    elif board.is_terminal():
        return (None, 0)
    elif depth == 0:
        return (None, heuristic_score(board))
    
    moves = board.get_actions()

    if player:
        v = -1000000000
        best_column = moves[0]
        for move in moves:
            row = board.find_row_index(move)
            board_copy = copy.deepcopy(board)
            board_copy.board[row][move] = board_copy.turn
            board_copy.change_player()
            board_copy.previous_move = [row, move]
            new_score = minimax(board_copy, depth - 1, alpha, beta, False)[1]
            if new_score > v:
                v = new_score
                best_column = move
            alpha = max(alpha, new_score)
            if beta <= alpha:
                break
        return best_column, v

    else:
        v = 1000000000
        best_column = moves[0]
        for move in moves:
            row = board.find_row_index(move)
            board_copy = copy.deepcopy(board)
            board_copy.board[row][move] = board_copy.turn
            board_copy.change_player()
            board_copy.previous_mvoe = [row, move]
            new_score = minimax(board_copy, depth - 1, alpha, beta, True)[1]
            if new_score < v:
                v = new_score
                best_column = move
            beta = min(beta, new_score)
            if beta <= alpha:
                break
        return best_column, v





def count(area, player):
    count = 0
    for place in area:
        if place == player:
            count+=1
    return count


def evaluate(area, player):
    score = 0
    if player == 2:
        opp_player = 1
    else:
        opp_player = 2

    if count(area, player) == 4:
        score += 100000
    elif count(area, player) == 3 and count(area, 0) == 1:
        score += 5
    elif count(area, player) == 2 and count(area, 0) == 2:
        score += 2
    if count(area, opp_player) == 3 and count(area, 0) == 1:
        score -= 1000
    return score


def heuristic_score(b):
    score = 0
    area = []

    for r in range(0, 6):
        for c in range(0, 4):

            area.append(b.board[r][c])
            area.append(b.board[r][c+1])
            area.append(b.board[r][c+2])
            area.append(b.board[r][c+3])
            score += evaluate(area, b.turn)
            area = []

    for r in range(0, 3):
        for c in range(0, 7):
            area.append(b.board[r][c])
            area.append(b.board[r+1][c])
            area.append(b.board[r+2][c])
            area.append(b.board[r+3][c])
            score += evaluate(area, b.turn)
            area = []
    
    for r in range(0, 3):
        for c in range(0, 4):
            area.append(b.board[r][c])
            area.append(b.board[r+1][c+1])
            area.append(b.board[r+2][c+2])
            area.append(b.board[r+3][c+3])
            score += evaluate(area, b.turn)
            area = []

    for r in range(0, 3):
        for c in range(3, 7):
            area.append(b.board[r][c])
            area.append(b.board[r+1][c-1])
            area.append(b.board[r+2][c-2])
            area.append(b.board[r+3][c-3])
            score += evaluate(area, b.turn)
            area = []
    
    return score



        

# def heuristic_score(b):
#     #to be written
#     score = 0

#     #verticals
#     for row in range(0, 4):
#         for col in range(0, 7):
#             if b.board[row][col] == b.board[row+1][col] == b.board[row+2][col] == 2:
#                 score += 100
#             elif b.board[row][col] == b.board[row+1][col] == 2 or b.board[row+1][col] == b.board[row+2][col] == 2:
#                 score += 25
#             if b.board[row][col] == b.board[row+1][col] == b.board[row+2][col] == 1:
#                 score -= 1000
#             elif  b.board[row][col] == b.board[row+1][col] == 1 or b.board[row+1][col] == b.board[row+2][col] == 1:
#                 score -= 25
    
#     #horizontals
#     for row in range(0, 6):
#         for col in range(0, 5):
#             if b.board[row][col] == b.board[row][col+1] == b.board[row][col+2] == 2:
#                 score += 100
#             elif b.board[row][col] == b.board[row][col+1] == 2 or b.board[row][col+1] == b.board[row][col+2] == 2:
#                 score += 25
#             if b.board[row][col] == b.board[row][col+1] == b.board[row][col+2] == 1:
#                 score -= 1000
#             elif b.board[row][col] == b.board[row][col+1] == 1 or b.board[row][col+1] == b.board[row][col+2] == 1:
#                 score -= 25
    
#     #diagonals
#     for row in range(0, 4):
#         for col in range(0, 5):
#             if b.board[row][col] == b.board[row+1][col+1] == b.board[row+2][col+2] == 2:
#                 score += 100
#             elif b.board[row][col] == b.board[row+1][col+1] == 2 or b.board[row+1][col+1] == b.board[row+2][col+2] == 2:
#                 score += 25
#             if b.board[row][col] == b.board[row+1][col+1] == b.board[row+2][col+2] == 1:
#                 score -= 1000
#             elif b.board[row][col] == b.board[row+1][col+1] == 1 or b.board[row+1][col+1] == b.board[row+2][col+2] == 1:
#                 score -= 25
    
#     for row in range(0, 4):
#         for col in range(2, 7):
#             if b.board[row][col] == b.board[row+1][col-1] == b.board[row+2][col-2] == 2:
#                 score += 100
#             elif b.board[row][col] == b.board[row+1][col-1] == 2 or b.board[row+1][col-1] == b.board[row+2][col-2] == 2:
#                 score += 25
#             if b.board[row][col] == b.board[row+1][col-1] == b.board[row+2][col-2] == 1:
#                 score -= 1000
#             elif b.board[row][col] == b.board[row+1][col-1] == 1 or b.board[row+1][col-1] == b.board[row+2][col-2] == 1:
#                 score -= 25
#     return score



def findBestMove(board, depth):
    initial_board = AlphaBetaBoard(board)
    alpha = float('-inf')
    beta = float('inf')
    best_move = minimax(initial_board, depth, alpha, beta, True)[0]
    return best_move