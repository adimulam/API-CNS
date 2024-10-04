import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import logging

# Configure standard logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Load the dataset
df = pd.read_csv("../data/MedicalDatasetForModel.csv")
logger.info("Dataset loaded successfully.")
logger.info(f"DataFrame head:\n{df.head()}")

# Convert date columns to datetime format
pd.set_option('future.no_silent_downcasting', True)
df['Gender'] = df['Gender'].replace({'M': 0, 'F': 1}).astype(int)
df['Result'] = df['Result'].replace({'negative': 0, 'positive': 1}).astype(int)
logger.info("Converted Gender fields from M, F to 0,1.")
logger.info("Converted Results fields from negative,positive to 0,1.")

logger.info("saving normalized data back into a new csv file")
df.to_csv('../data/MedicalDatasetForModelNormalized.csv', index=False)

# Summary statistics
logger.info("Summary Statistics:")
logger.info(f"\n{df.describe(include='all')}")

# Checking for missing values
logger.info("Missing Values:")
logger.info(f"\n{df.isnull().sum()}")

# Data type information
logger.info("Data Types:")
logger.info(f"\n{df.dtypes}")