from copy import deepcopy


class ConnectFourBoard:
    def __init__(self, height=7, width=8):
        """ Instantiate Connect Four Board with an empty state """
        self._board = [[" " for _ in range(width)] for _  in range(height)]
        self._colors = ['R', 'B']
        self._HEIGHT, self._WIDTH = height, width

    def empty_board(self):
        """ Reset board state """
        self._board = [[" " for _ in range(self._WIDTH)] for _  in range(self._HEIGHT)]

    def print_board(self):
        """ Print board state """
        for _i in range(len(self._board)):
            for _j in range(len(self._board[_i])):
                if _j == 0:
                    print(_i, end=" ")
                print(self._board[_i][_j], end=" ")
            print("\n", end="")
        print("  ", end="")
        for _i in range(self._WIDTH):
            print(_i, end=" ")
        print("\n~~~~~~~~~~~~~~~~~~~")

    def make_move(self, column, color):
        """ Drop a piece in specified column """
        if column > self._WIDTH-1:
            raise Exception("Piece dropped in column > 7: Column -> {}".format(column))
        elif self._board[0][column] != " ":
            raise Exception("Piece dropped in full column: Column -> {}".format(column))
        elif color not in self._colors:
            raise Exception("Color not in list of possible colors: Color -> {}".format(color))
        for _i in reversed(range(self._HEIGHT)): ## Drop piece into column
            if self._board[_i][column] == " ":
                self._board[_i][column] = color
                break

    def check_for_win_state(self, board, color=None):
        """ Check board to see if there are any win-states """
        if color is None:
            for _color in self._colors:
                if self.highest_sequence(board, _color) == 4:
                    return _color
            return None
        return color if self.highest_sequence(board, color) == 4 else None

    def possible_game_states(self, board, color):
        """ Generate a list of all possible game states """
        if color not in self._colors:
            raise Exception("Color not in list of possible colors: Color -> {}".format(color))
        potential_game_states = list()
        for _i in range(self._WIDTH):  ## Drop piece into column
            for _k in range(self._HEIGHT):
                if board[_k][_i] == " ":
                    temp_board = deepcopy(board)
                    temp_board[_k][_i] = color
                    potential_game_states.append((temp_board, _i))
                    break
        return potential_game_states

    def highest_sequence(self, board, color):
        """ Check board to see if there are any win-states """
        highest_integer_sequence = 0
        _connect_four_cache = [" " for _ in range(4)]
        ### Check horizontal positions
        for _i in range(self._HEIGHT):
            for _k in range(self._WIDTH):
                _connect_four_cache.pop(0)
                _connect_four_cache.append(board[_i][_k])
                color_cache_size = _connect_four_cache.count(color)
                if color_cache_size == len(_connect_four_cache):
                    return 4
                elif color_cache_size > highest_integer_sequence:
                    highest_integer_sequence = color_cache_size
        _connect_four_cache = [" " for _ in range(4)]
        ### Check vertical positions
        for _i in range(self._WIDTH):
            for _k in range(self._HEIGHT):
                _connect_four_cache.pop(0)
                _connect_four_cache.append(board[_k][_i])
                color_cache_size = _connect_four_cache.count(color)
                if color_cache_size > highest_integer_sequence:
                    highest_integer_sequence = color_cache_size
        for _i in range(self._HEIGHT):
            _connect_four_cache = [" " for _ in range(4)]
            for _elem in [board[_i-_k][_k] for _k in range(_i+1)]:
                _connect_four_cache.pop(0)
                _connect_four_cache.append(_elem)
                color_cache_size = _connect_four_cache.count(color)
                if color_cache_size > highest_integer_sequence:
                    highest_integer_sequence = color_cache_size
        for _i in reversed(range(self._HEIGHT)):
            _connect_four_cache = [" " for _ in range(4)]
            for _elem in [board[_i+(self._WIDTH-1-_k)][_k] for _k in range(self._WIDTH)[_i+1:]]:
                _connect_four_cache.pop(0)
                _connect_four_cache.append(_elem)
                color_cache_size = _connect_four_cache.count(color)
                if color_cache_size > highest_integer_sequence:
                    highest_integer_sequence = color_cache_size
        _connect_four_cache = [" " for _ in range(4)]
        for _i in reversed(range(self._HEIGHT)):
            for _elem in [board[self._HEIGHT-1-_i][_k] for _k in range(self._WIDTH)]:
                _connect_four_cache.pop(0)
                _connect_four_cache.append(_elem)
                color_cache_size = _connect_four_cache.count(color)
                if color_cache_size > highest_integer_sequence:
                    highest_integer_sequence = color_cache_size
        return highest_integer_sequence


def player_vs_BOT(bot_make_move_function):
    move = 0
    board = ConnectFourBoard()
    teams = board._colors
    while board.check_for_win_state(board._board) is None:
        board.print_board()
        if move == 0:  ### Player move
            column = int(input("Select column number: "))
        else:  ### BOT move
            column = bot_make_move_function(board.possible_game_states(board._board, teams[move]), teams[move], board, _turn='B')
        if column != -1:
            board.make_move(column, teams[move])
            move = (move + 1)%2
    print("Winner: ", board.check_for_win_state(board._board))
























