import data_loader
from quantum_autoencoder_circuit import QuantumAutoencoder
import numpy as np
import matplotlib.pyplot as plt

# Load the training and signal datasets
training_data = data_loader.load_h5_dataset('path_to_training_data.h5', 'training_dataset')
signal_data = data_loader.load_h5_dataset('path_to_signal_data.h5', 'signal_dataset')

# Initialize the quantum autoencoder
n_qubits = 4
layers = 2
circuit_type = 'default'  # or 'custom'
autoencoder = QuantumAutoencoder(n_qubits, layers, circuit_type)

# Load the parameters of the trained quantum autoencoder
params = np.load('path_to_saved_params.npy')

# Define the reconstruction function
def reconstruct(x, params):
    return autoencoder.autoencoder_circuit(x, params)

# Calculate the reconstruction error for each signal
reconstruction_errors = []
for signal in signal_data:
    reconstructed_signal = reconstruct(signal, params)
    error = np.mean((signal - reconstructed_signal) ** 2)
    reconstruction_errors.append(error)

# Plot the error distribution histograms
plt.hist(reconstruction_errors, bins=50, alpha=0.75)
plt.xlabel('Reconstruction Error')
plt.ylabel('Frequency')
plt.title('Reconstruction Error Distribution')
plt.show()
