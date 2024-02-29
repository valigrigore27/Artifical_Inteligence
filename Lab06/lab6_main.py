import itertools


def initialize_game():
    state = {
        'player1': [],
        'player2': [],
        'current_player': 'player1',
        'available_numbers': list(range(1, 10)),
    }
    return state


def display_board(state):
    player1_numbers = ", ".join(map(str, state['player1']))
    player2_numbers = ", ".join(map(str, state['player2']))

    print(f"Player 1: {player1_numbers}")
    print(f"Player 2: {player2_numbers}")
    print(f"Current Player: {state['current_player']}")
    print(f"Available Numbers: {state['available_numbers']}")
    print("--------------------------------------------------------------------||")


def is_available(state, number):
    if number not in state['available_numbers']:
        print("Choose another available number.")
        return False

    if state['current_player'] == 'player1':
        state['player1'].append(number)
    else:
        state['player2'].append(number)

    state['available_numbers'].remove(number)

    return True


def switch_player(state):
    state['current_player'] = 'player1' if state['current_player'] == 'player2' else 'player2'


def check_winner(state):
    player = state['current_player']
    player_numbers = state[player]

    if len(player_numbers) < 3:
        return False

    for combo in itertools.combinations(player_numbers, 3):
        if sum(combo) == 15:
            return True

    return False


def recommend_number(state):
    current_player = state['current_player']
    opponent = 'player1' if current_player == 'player2' else 'player2'

    if len(state[opponent]) >= 2:

        for combo in itertools.combinations(state[opponent], 2):

            for number in state['available_numbers']:

                if sum(combo) + number == 15:
                    return number

    return None

def is_draw(state):
    return len(state['available_numbers']) == 0


state = initialize_game()
while True:
    display_board(state)
    if state['current_player'] == 'player1':
        recommended_number = recommend_number(state)
        if recommended_number is not None:
            print("!!WARNING!! Do you want to prevent the opponent from winning? y/n")
            answer = input()
            if answer == 'y':
                print(f"Choose number {recommended_number} !")
    number = int(input(f"{state['current_player']}, choose a number from available numbers: "))

    if is_available(state, number):
        if check_winner(state):
            display_board(state)
            print(f"{state['current_player']} won!")
            break
        elif is_draw(state):
            display_board(state)
            print("DRAW!")
            break
        switch_player(state)
