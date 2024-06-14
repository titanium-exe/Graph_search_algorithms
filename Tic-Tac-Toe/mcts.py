# MCTS algorithm implementation


# packages
import math
import random


# tree node class definition
class TreeNode:
    def __init__(self, board, parent=None):
        # init associated board states
        self.board = board

        # is node terminal --> won or drawn(flag)
        if self.board.is_win() or self.board.is_draw():
            # we have the terminal node
            self.terminal = True
        else:
            self.terminal = False

        # fully expanded
        self.is_fully_expanded = self.terminal

        # init parent node if available
        self.parent = parent

        # init score and visits
        self.visits = 0
        self.total_score = 0

        # init current node's children
        self.children = {}


# MCTS class
class MCTS:
    # search for the best move in the current position
    def search(self, initial_state):
        # create root node
        self.root = TreeNode(initial_state, None)

        # search 1000 iterations
        for iterations in range(1000):
            # select a node --> SELECTION PHASE
            node = self.select(self.root)

            # SIMULATION PHASE
            score = self.rollout(node.board)

            # Backpropagation : the score the # visits and score to the root node
            self.backpropogate(node, score)

            # pickup the best move in the current position
            try:
                return self.get_best_move(self.root, 0)
            except Exception as e:
                pass

    # select most promising node
    def select(self, node):
        pass

    # simulate the game by making random moves until reach end of the game
    def rollout(self, board):
        pass

    def backpropogate(self, node, score):
        pass

    # Select the best node bases on UCB1/UCT formula
    # we need to loop over child nodes of the below node taken as parameter
    def get_best_move(self, node, exploration_constant):
        # define best score and best moves
        best_score = float('-inf')
        best_moves = []

        # loop over child nodes
        for child_node in node.children.values():
            # define current player
            if child_node.board.player_2 == 'x':
                current_player = 1
            if child_node.board.player_2 == 'o':
                current_player = -1

        # get move score using UCT formula
        move_score = current_player * child_node.score / child_node.visits + exploration_constant * math.sqrt(
            math.log(node.visits) / child_node.visits)

        # better move has been found
        if move_score > best_score:
            best_score = move_score
            best_moves = [child_node]

        # found as good move as already available
        elif move_score == best_score:
            best_moves.append(child_node)

        # return one of the best moves randomly
        return random.choice(best_moves)
