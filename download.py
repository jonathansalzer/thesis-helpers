# DOWNLOADS A RLDS DATASET FROM GOOGLE CLOUD STORAGE

import tensorflow_datasets as tfds
import tqdm

# optionally replace the DATASET_NAMES below with the list of filtered datasets from the google sheet
DATASET_NAMES = ['nyu_rot_dataset_converted_externally_to_rlds']
DOWNLOAD_DIR = '~/tensorflow_datasets'

print(f"Downloading {len(DATASET_NAMES)} datasets to {DOWNLOAD_DIR}.")
for dataset_name in tqdm.tqdm(DATASET_NAMES):
  _ = tfds.load(dataset_name, data_dir=DOWNLOAD_DIR)
