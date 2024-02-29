import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

file_path = "C:/Users/Tuf/OneDrive/Desktop/Ai/TEMA-lab7-aiabun/seeds_dataset.txt"
column_names = ["Atribut1", "Atribut2", "Atribut3", "Atribut4", "Atribut5", "Atribut6", "Atribut7", "Clasa"]
data = pd.read_csv(file_path, delimiter='\t', header=None, names=column_names)

X = data.drop("Clasa", axis=1)
y = data["Clasa"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print()
print("Date de antrenare:")
print(X_train)

print("\nDate de testare:")
print(X_test)
print()

# #####################################################################################################################################


input_size = X_train.shape[1]

hidden_size = 5

output_size = len(np.unique(y_train))

learning_rate = 0.01

num_epochs = 1000

np.random.seed(42)

weights_input_hidden = np.random.randn(input_size, hidden_size)
weights_hidden_output = np.random.randn(hidden_size, output_size)

print("Ponderi intrare - ascuns:", weights_input_hidden.shape)
print("Ponderi ascuns - ieșire:", weights_hidden_output.shape)
print()


# #######################################################################################################

def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    return x * (1 - x)


def sigmoid_output(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_output_derivative(x):
    return x * (1 - x)


def softmax(x):
    exp_x = np.exp(x - np.max(x, axis=-1, keepdims=True))
    return exp_x / np.sum(exp_x, axis=-1, keepdims=True)


def softmax_derivative(x):
    return None


def cross_entropy(y_true, y_pred):
    epsilon = 1e-15
    y_pred = np.clip(y_pred, epsilon, 1 - epsilon)
    return - (y_true * np.log(y_pred)).sum(axis=-1)


def cross_entropy_derivative(y_true, y_pred):
    return y_pred - y_true
