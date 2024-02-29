import numpy as np

num_rows = 7
num_cols = 10

start_state = (3, 0)
goal_state = (3, 7)
wind = [0, 0, 0, 1, 1, 1, 2, 2, 1, 0]

alpha = 0.5
gamma = 0.1
epsilon = 0.1

Q = np.zeros((num_rows, num_cols, 4))


def choose_action(state):
    if np.random.rand() < epsilon:
        return np.random.choice(4)
    else:
        return np.argmax(Q[state])


def take_action(state, action):
    row, col = state
    if action == 0:  # sus
        row -= 1
    elif action == 1:  # jos
        row += 1
    elif action == 2:  # stânga
        col -= 1
    elif action == 3:  # dreapta
        col += 1

    row += wind[col % len(wind)]
    row = max(0, min(row, num_rows - 1))
    col = max(0, min(col, num_cols - 1))
    return row, col


num_episodes = 4

for episode in range(num_episodes):
    state = start_state

    while state != goal_state:
        action = choose_action(state)
        new_state = take_action(state, action)
        reward = -1
        Q[state][action] = Q[state][action] + alpha * (reward + gamma * np.max(Q[new_state]) - Q[state][action])
        state = new_state

print()
print(Q)
print()
