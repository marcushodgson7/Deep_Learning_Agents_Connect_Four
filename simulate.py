import mcts_agent
from mainboard import MainBoard
import alphabeta_agent
from argparse import ArgumentParser, ArgumentError
import sys



def simulate_time(time1, time2):

    game = MainBoard()

    while game.is_terminal() == False:
        if game.turn == 1:
            best_child = mcts_agent.findBestMove(game.board)

            game.board[best_child[0]][best_child[1]] = game.turn
            game.previous_move = [best_child[0], best_child[1]]

            if game.win() != None:
                print_board(game)
                print('player 1 won')
                break

            print_board(game)
            game.change_player()

        else:

            col = int(input('make a move from 0-6\n'))
            row = game.find_row_of_move(col)

            game.board[row][col] = game.turn
            game.previous_move = [row, col]

            if game.win() != None:
                print_board(game)
                print('player 2 won')
                break

            print_board(game)
            game.change_player()



        
    


def simulate_alphabeta(sims1, sims2):

    game = MainBoard()

    while game.is_terminal() == False:
        if game.turn == 1:
            col = int(input('make a move from 0-6\n'))
            row = game.find_row_of_move(col)

            game.board[row][col] = game.turn
            game.previous_move = [row, col]

            if game.win() != None:
                print_board(game)
                print('player 1 won')
                break

            print_board(game)
            game.change_player()

        else:
            col = alphabeta_agent.findBestMove(game.board, 6)
            row = game.find_row_of_move(col)

            game.board[row][col] = game.turn
            game.previous_move = [row, col]

            if game.win() != None:
                print_board(game)
                print('player 2 won')
                break

            print_board(game)
            game.change_player()



def simulate_both():

    game = MainBoard()

    while game.is_terminal() == False:
        if game.turn == 1:
            best_child = mcts_agent.findBestMove(game.board)
            game.board[best_child[0]][best_child[1]] = game.turn
            game.previous_move = [best_child[0], best_child[1]]
            if game.win() != None:
                return 1
            game.change_player()
        else:
            col = alphabeta_agent.findBestMove(game.board, 6)
            row = game.find_row_of_move(col)
            game.board[row][col] = game.turn
            game.previous_move = [row, col]
            if game.win() != None:
                return 2
            game.change_player()
    return 0


def print_board(game):
    for i in game.board:
        print(i)



def test():
    pass


def main():
    parser = setup_argument_parser()
    try:
        args = vars(parser.parse_args())
    except ArgumentError as arg_err:
        print(arg_err, file=sys.stderr)
        sys.exit(1)

    #simulate_time(args['time1'], args['time2'])

    simulate_time(10, 10)

    #test()
    #game = Game()
    #print(game.get_board())


def setup_argument_parser():
    parser = ArgumentParser(description='Connect Four with MCTS and Alpha-Beta Pruning', allow_abbrev=False)
    parser.add_argument('time1', metavar='time1', default=None, type=int, help='Time allowed to run simulations for Agent 1 (MCTS algorithm)')
    parser.add_argument('time2', metavar='time2', default=None, type=int, help='Time allowed to run simulations for Agent 2 (Alpha-Beta Pruning)')
    parser.add_argument('sims1', metavar='sims1', default=None, type=int, help='Number of simulations allowed for Agent 1 (MCTS algorithm)')
    parser.add_argument('sims2', metavar='sims2', default=None, type=int, help='Number of simulations allowed for Agent 2 (Alpha-Beta Pruning)')
    parser.add_argument('type', metavar='type', default=None, choices=['both', 'time', 'simulations'], type=str, 
        help='"both" to use run time and simulations, "time" to only use run time, and "simulations" to only use number of simulations')
    return parser

if __name__ == '__main__':
    main()