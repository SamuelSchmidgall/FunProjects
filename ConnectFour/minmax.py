from connect_four import ConnectFourBoard, player_vs_BOT

def board_heuristic(states, _board, color):
    """ Value between -1 and 1 with 1 indicating a winning position and -1 a losing position """
    return [_board.highest_sequence(_state[0], color)/4 for _state in states]

def min_max(states, color, _board, depth=0, max_depth=4, _turn=None):
    if depth == max_depth:
        if _turn == color:
            return max(board_heuristic(states, _board, _turn))
        else:
            return -max(board_heuristic(states, _board, _turn))
    else:
        if depth == 0:
            if _turn == color:
                val = [min_max(_board.possible_game_states(_state[0], _turn), color, _board, depth=depth+1, max_depth=max_depth, _turn=[_ for _ in _board._colors if _ != _turn][0]) if _board.check_for_win_state(_state[0]) is None else (-1 if _board.check_for_win_state(_state[0]) != color else 1) for _state in states]
                return val.index(max(val))
            else:
                val = [min_max(_board.possible_game_states(_state[0], _turn), color, _board, depth=depth+1, max_depth=max_depth, _turn=[_ for _ in _board._colors if _ != _turn][0]) if _board.check_for_win_state(_state[0]) is None else (-1 if _board.check_for_win_state(_state[0]) != color else 1) for _state in states]
                return val.index(min(val))
        else:
            if _turn == color:
                return max([min_max(_board.possible_game_states(_state[0], _turn), color, _board, depth=depth+1, max_depth=max_depth, _turn=[_ for _ in _board._colors if _ != _turn][0]) if _board.check_for_win_state(_state[0]) is None else (-1 if _board.check_for_win_state(_state[0]) != color else 1) for _state in states])
            else:
                return -max([min_max(_board.possible_game_states(_state[0], _turn), color, _board, depth=depth+1, max_depth=max_depth, _turn=[_ for _ in _board._colors if _ != _turn][0]) if _board.check_for_win_state(_state[0]) is None else (-1 if _board.check_for_win_state(_state[0]) != color else 1) for _state in states])



player_vs_BOT(min_max)





