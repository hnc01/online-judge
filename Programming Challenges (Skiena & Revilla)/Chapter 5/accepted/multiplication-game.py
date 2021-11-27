# mapping number to who can win
can_win = {}


def get_winner(n, p, player):
    global can_win

    # we know that given p, the user can multiply it by any number between 2 and 9
    for i in range(2, 10):
        if p * i >= n:
            # the current player hit the target and maybe more so he wins
            return player

        if (p * i) in can_win:
            # it means we already processed this product before and we know who won
            # can the given player (always Stan since we started the function with him) win this?
            if can_win[p * i]:
                return player
        else:
            # is the winner Stan?
            can_win[p * i] = get_winner(n, p * i, not player) == player

            if can_win[p * i]:
                return player

    # if none of above returns worked then our player can't win
    return not player


while True:
    try:
        # target number
        n = int(input())

        # stan is False and ollie is True
        player = False

        # stan always starts with p = 1
        p = 1

        # basically we're checking if the given player can win this
        # so we're always checking from point of view of Stan
        winner = get_winner(n, p, player)

        if not winner:
            print("Stan wins.")
        else:
            print("Ollie wins.")

        # reset the dp map
        can_win = {}

    except EOFError:
        break
