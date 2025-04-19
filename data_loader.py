import h5py

def load_h5_dataset(file_path, dataset_name):
    with h5py.File(file_path, 'r') as file:
        dataset = file[dataset_name][:]
    return dataset
