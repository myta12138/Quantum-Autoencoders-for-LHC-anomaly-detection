# Quantum-Autoencoders-for-LHC-anomaly-detection

## Introduction

This repository contains code and files related to building a quantum autoencoder using Pennylane and using reconstruction error for anomaly detection. The quantum autoencoder is trained on a dataset and then used to reconstruct signals. The reconstruction error is used to detect anomalies in the signals.

## Requirements

To install the required packages, run:
```
pip install -r requirements.txt
```

## Usage

### Training the Quantum Autoencoder

1. Load the training and signal datasets using the `data_loader` module.
2. Initialize the quantum autoencoder using the `QuantumAutoencoder` class from the `quantum_autoencoder_circuit` module.
3. Train the quantum autoencoder on the training dataset using the `training.py` script.
4. Save the parameters of the trained quantum autoencoder.

### Anomaly Detection

1. Load the training and signal datasets using the `data_loader` module.
2. Load the parameters of the trained quantum autoencoder.
3. Reconstruct the signal datasets using the quantum autoencoder.
4. Calculate the reconstruction error for each signal.
5. Use the reconstruction errors to plot error distribution histograms and detect anomalies.

## Files

- `requirements.txt`: Contains the required packages for the project.
- `data_loader.py`: Contains the function to load datasets from h5 files.
- `quantum_autoencoder_circuit.py`: Contains the implementation of the quantum autoencoder using Pennylane.
- `training.py`: Script to train the quantum autoencoder on the training dataset.
- `reconstruct.py`: Script to reconstruct the signal datasets and calculate the reconstruction error.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
