import random
from connect_four import player_vs_BOT


def monte_carlo(states, color, _board, depth=0, max_depth=100, _turn=None):
    """ Monte Carlo simulation heuristic for Connect Four """
    if depth == 0:
        state_scores = list()
        for state in states:
            mc_heuristic = monte_carlo(state, color, _board, depth=1, max_depth=max_depth, _turn=[_color for _color in _board._colors if _color != color][0])
            try:
                state_scores.append(sum(mc_heuristic)/len(mc_heuristic))
            except ZeroDivisionError:
                state_scores.append(0.0)
        return state_scores.index(max(state_scores))
    elif depth == max_depth:
        return list()
    branch = 2 if random.uniform(0, 1) > depth/max_depth + 0.8 else 1
    states = [state if _board.check_for_win_state(state[0]) is None else (0 if _board.check_for_win_state(state[0]) != color else 1) for state in _board.possible_game_states(states[0], _turn)]
    non_win_states, win_states = [state for state in states if type(state) != int], [state*(max_depth-depth)/max_depth for state in states if type(state) == int]
    if len(non_win_states) > 0:
        for _ in range(branch):
            win_states += monte_carlo(random.choice(non_win_states), color, _board, depth=depth+1, max_depth=max_depth, _turn=[_color for _color in _board._colors if _color != _turn][0])
        return win_states
    return list()





player_vs_BOT(monte_carlo)














