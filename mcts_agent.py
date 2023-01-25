
import random
import math
import copy
import time
from mctsboard import MCTSBoard


class Node():
#data structure that records the state of the game, parent Node, children Node, and move that it took to get to that state
    def __init__(self, state: MCTSBoard, parent = None):
        self.visits = 1 
        self.payoff = 0.0
        self.state = state
        self.parent = parent
        self.children = []
        self.moves_to_children = []

    def update_children(self, child_node, move):
        #updates the node with a new child node by giving a state made by a specific move
        self.children.append(child_node)
        self.moves_to_children.append(move)

    def update(self, payoff):
        #TO CODE
        self.visits += 1
        if self.state.turn == 1:
            self.payoff -= payoff
        else:
            self.payoff += payoff



def mcts_policy(maxIter, root_node: Node):
    for i in range(maxIter):
        #TRAVERSE THE TREE
        leaf = find_leaf(root_node)

        #SIMULATE
        payoff = simulate_game(leaf.state)

        #UPDATE
        update_node(leaf, payoff)

    best_node = next_node(root_node, False)
    return best_node


def find_leaf(current: Node):
    #finds a leaf that will be simulated
    while current.state.is_terminal() == False and current.state.win() == 0:
        if len(current.children) != len(current.state.get_actions()):
            #EXPAND THE LEAF
            return expand_leaf(current)
        else:
            current = next_node(current)
    return current

def expand_leaf(leaf_node: Node):
    #expands the leaf if it is not fully expanded
    moves = leaf_node.state.get_actions()
    for move in moves:
        if move not in leaf_node.moves_to_children:
            new_state = copy.deepcopy(leaf_node.state)
            row = leaf_node.state.find_row_index(move)
            new_state.board[row][move] = leaf_node.state.turn 
            new_state.change_player()
            new_state.previous_move = [row, move]
            new_node = Node(new_state, leaf_node)
            leaf_node.update_children(new_node, move)
            return new_node

def next_node(node: Node, explore_bool = True):
    #finds the next best node based on the ucb value
    ucb_list = []
    for child in node.children:
        exploit = child.payoff/child.visits
        explore = 0
        if explore_bool == True:
            explore = math.sqrt(math.log(2.0*node.visits)/float(child.visits))
        ucb = exploit + 2 * explore
        ucb_list.append(ucb)
    return node.children[ucb_list.index(max(ucb_list))]

def simulate_game(state: MCTSBoard):
    #simulates a game until finished and returns the final result
    while state.is_terminal() == False and state.win() == 0:
        state = state.successor()
    return state.win()

def update_node(curr: Node , payoff):
    #goes back up through the data structure and updates the visits and payoffs of each node based on the state results
    while curr != None:
        curr.update(payoff)
        curr = curr.parent




def findBestMove(board):
    initial_board = MCTSBoard(board)
    # Returns the best move using MonteCarlo Tree Search
    initial_node = Node(initial_board)
    best_node = mcts_policy(4000, initial_node)
    return best_node.state.previous_move


