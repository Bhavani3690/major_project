from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
import numpy as np

model = Sequential([
    Flatten(input_shape=(64,64,3)),
    Dense(128, activation='relu'),
    Dense(3, activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy')

# Dummy training
X = np.random.rand(10,64,64,3)
y = np.random.rand(10,3)

model.fit(X, y, epochs=1)

model.save("model.h5")

print("Model created successfully!")