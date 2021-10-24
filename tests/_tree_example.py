"""
        Define a graph we know the answer to, make sure we hit the right answer
        This is the same test as the one used in minimax, because both should
        probably come to the same answer in this case
                                          a
                                 a1   /---|----\\    a3
                              /-------    |     -------\\
                          ----         a2 |             ----
                          |               |                |
                          |               |                |
                        3 b             3 c              4 d
                        /-|-\\            /|\\              /|\\
                    b1 /  |  \\ b3       / | \\ c3     d1  / | \\ d3
                      / b2|   \\      c1/  |  \\          /  |  \\
                     /    |    \\      / c2|   \\        / d2|   \\
                    /     |     \\    /    |    \\      /    |    \\
                   -             -  -           -    -     |     -
                 3 e    12f    8 g  2 h   4i    6j   14k   5l    2m
        Note that node k, with a score of 14 doesn't get selected. This is because
        we assume that the opponent is trying to pick the optimal means to minimize
        the score, so we take the conservative route of picking a1 since it has the
        'least worst' outcome

        If you were to adjust node m to have a terminal value of 3, it would still
        return the a1, even if there's a greater potential node if we took a3, since
        we assume the opponent will select the optimal move on their end, they're
        equivalent


"""
from math import inf


def terminal_side_effect(state, depth_remaining, time_remaining):
    """ Side effect returns true if we reach a terminal state

    :param state: the state of the game to evaluate
    :param depth_remaining: true if there is depth remaining
    :param time_remaining: true if there is time remaining
    :return: true if we are terminating
    """
    if not depth_remaining:
        return True
    end_state_nodes = []
    for alpha in list(map(chr, range(101, 110))):  # iterate from e-m
        end_state_nodes.append(str(alpha))
    if state in end_state_nodes:
        return True
    return False


def eval_side_effect(state):
    """ Side effect returns an evaluation given a state

    :param state: the current state to evaluate
    :return: a score for the current state
    """
    match state:
        case "a":
            val = inf  # this is our root note, it shouldn't get a score
        case "b":
            val = 3
        case "c":
            val = 3
        case "d":
            val = 4
        case "e":
            val = 3
        case "f":
            val = 12
        case "g":
            val = 8
        case "h":
            val = 2
        case "i":
            val = 4
        case "j":
            val = 6
        case "k":
            val = 14
        case "l":
            val = 5
        case "m":
            val = 2
        case _:
            val = -inf  # this shouldn't happen in our simple case
    return val


def actions_side_effect(state):
    """ Side effect for actions, returns the actions available for a given state

    :param state: the current state
    :return: actions available for the given state
    """
    match state:
        case "a":
            val = ["a1", "a2", "a3"]
        case "b":
            val = ["b1", "b2", "b3"]
        case "c":
            val = ["c1", "c2", "c3"]
        case "d":
            val = ["d1", "d2", "d3"]
        case "e":
            val = []
        case "f":
            val = []
        case "g":
            val = []
        case "h":
            val = []
        case "i":
            val = []
        case "j":
            val = []
        case "k":
            val = []
        case "l":
            val = []
        case "m":
            val = []
        case _:
            val = None  # This shouldn't happen
    return val


def result_side_effect(state, action):
    """ Side effect for result, returns the resulting state given an action

    :param state: the current state
    :param action: the action to take
    :return: the new state given the action
    """
    match action:
        # We would normally evaluate this with the
        # state to determine validity, etc, but this is a pre-established graph
        case "a1":
            val = "b"
        case "a2":
            val = "c"
        case "a3":
            val = "d"
        case "b1":
            val = "e"
        case "b2":
            val = "f"
        case "b3":
            val = "g"
        case "c1":
            val = "h"
        case "c2":
            val = "i"
        case "c3":
            val = "j"
        case "d1":
            val = "k"
        case "d2":
            val = "l"
        case "d3":
            val = "m"
        case _:
            val = None  # default case, shouldn't happen
    return val