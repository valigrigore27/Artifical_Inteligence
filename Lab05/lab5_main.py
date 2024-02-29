import numpy as np
from sklearn.model_selection import train_test_split

# Citirea datelor din fișier
file_path = "calea/catre/fisier.txt"
data = np.loadtxt(file_path)

# Separarea atributelor și claselor
X = data[:, :-1]  # Atributele
y = data[:, -1]   # Clasele

# Împărțirea setului de date în date de antrenare și de testare
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Verificarea dimensiunilor seturilor de date
print("Dimensiunile setului de antrenare:", X_train.shape, y_train.shape)
print("Dimensiunile setului de testare:", X_test.shape, y_test.shape)
