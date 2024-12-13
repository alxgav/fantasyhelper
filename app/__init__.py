import os

from config.config import DATA_DIR

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)
