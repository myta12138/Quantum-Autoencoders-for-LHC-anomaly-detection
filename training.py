import data_loader
from quantum_autoencoder_circuit import QuantumAutoencoder
import numpy as np

# Load the training and signal datasets
training_data = data_loader.load_h5_dataset('path_to_training_data.h5', 'training_dataset')
signal_data = data_loader.load_h5_dataset('path_to_signal_data.h5', 'signal_dataset')

# Initialize the quantum autoencoder
n_qubits = 4
layers = 2
circuit_type = 'default'  # or 'custom'
autoencoder = QuantumAutoencoder(n_qubits, layers, circuit_type)

# Define the cost function
def cost(params, x):
    reconstructed = autoencoder.autoencoder_circuit(x, params)
    return np.mean((x - reconstructed) ** 2)

# Train the quantum autoencoder
opt = qml.GradientDescentOptimizer(stepsize=0.1)
epochs = 100
for epoch in range(epochs):
    for x in training_data:
        params = opt.step(lambda v: cost(v, x), autoencoder.params)
    if epoch % 10 == 0:
        print(f'Epoch {epoch}: cost = {cost(autoencoder.params, training_data[0])}')
        np.save(f'params_epoch_{epoch}_{circuit_type}.npy', autoencoder.params)
