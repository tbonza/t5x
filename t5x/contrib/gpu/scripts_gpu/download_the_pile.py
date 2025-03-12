import tensorflow_datasets as tfds

# This will download 'ThePile' to TFDS_DATA_DIR (environment variable).
ds = tfds.load("ThePile")
