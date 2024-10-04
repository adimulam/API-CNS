import pandas as pd
import numpy as np
import logging
from matplotlib import pyplot as plt
import io
import base64

# Configure standard Python logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

df = pd.read_csv("../data/MedicalDatasetForModelNormalized.csv")
logger.info("Dataset loaded for binning.")

categories = {
    'Age': ['Juvenile', 'Adult', 'Middle Age', 'Senior Citizen'],
    'HeartRate': ['Low', 'Normal', 'High'],
    'BloodSugar': ['Low', 'Normal', 'High']
}

bin_sizes = {
    'Age': 5,
    'HeartRate': 4,
    'BloodSugar': 4
}

def plot_distance_bins(x):
    # Distance binning
    min_value = df[x].min()
    max_value = df[x].max()
    logger.info(f"Min {x}: {min_value}, Max {x}: {max_value}")

    bins = np.round(np.linspace(min_value, max_value, bin_sizes[x]), 3)
    logger.info(f"Bins: {bins}")

    labels = categories[x]

    # Cut function for distance binning
    df['bins_dist'] = pd.cut(df[x], bins=bins, labels=labels, include_lowest=True)
    logger.info(f"Distance Binning Results:\n{df['bins_dist']}")

    combined_labels = [f'{labels[i]} ({bins[i]}-{bins[i+1]})' for i in range(len(labels))]

    plt.figure(figsize=(12, 6))

    # Plot histogram with 4 bins
    counts, _, patches = plt.hist(df['bins_dist'].cat.codes, bins=np.arange(len(labels) + 1) - 0.5, edgecolor='black')
    plt.xticks(ticks=np.arange(len(labels)), labels=combined_labels, ha='center')  # Set x-ticks to category labels

    # Annotate the histogram bars with their heights
    for count, patch in zip(counts, patches):
        height = patch.get_height()
        plt.text(patch.get_x() + patch.get_width() / 2, height, str(int(height)), 
                ha='center', va='bottom')  # ha: horizontal alignment, va: vertical alignment


    # Adding labels and title
    plt.xlabel(x)
    plt.ylabel('Number of Records')
    plt.title(str(x) + ' - Distance Binning')

    # Save the plot to a buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)

    # Encode the image in base64 and log it
    img_base64 = base64.b64encode(buf.read()).decode('utf-8')

    # Save the plot as a file
    output_filename = '../output/Binning_Distance_' + str(x)
    plt.savefig(output_filename)
    logger.info("Binning plot saved as" + str(output_filename))

    # Close the buffer
    buf.close()
    plt.close()


def plot_frequency_bins(x):
    # Distance binning
    min_value = df[x].min()
    max_value = df[x].max()
    logger.info(f"Min {x}: {min_value}, Max {x}: {max_value}")

    # Sort the data for quantile-based binning
    sorted_data = np.sort(df[x])

    # Define the number of bins (e.g., bin_sizes[x])
    num_bins = bin_sizes[x]

    # Get the bin edges using quantiles
    bins = np.round(np.quantile(sorted_data, np.linspace(0, 1, num_bins + 1, 3)))
    logger.info(f"Bins: {bins}")

    labels = categories[x]

    # Frequency binning
    df['bin_freq'] = pd.qcut(df[x], q=bin_sizes[x]-1, precision=1, labels=labels)
    logger.info(f"Frequency Binning Results:\n{df['bin_freq']}")

    combined_labels = [f'{labels[i]} ({bins[i]}-{bins[i+1]})' for i in range(len(labels))]

    plt.figure(figsize=(12, 6))

    # Plot histogram with 4 bins
    counts, _, patches = plt.hist(df['bin_freq'].cat.codes, bins=np.arange(len(labels) + 1) - 0.5, edgecolor='black')
    plt.xticks(ticks=np.arange(len(labels)), labels=combined_labels, ha='center')  # Set x-ticks to category labels

    # Annotate the histogram bars with their heights
    for count, patch in zip(counts, patches):
        height = patch.get_height()
        plt.text(patch.get_x() + patch.get_width() / 2, height, str(int(height)), 
                ha='center', va='bottom')  # ha: horizontal alignment, va: vertical alignment


    # Adding labels and title
    plt.xlabel(x)
    plt.ylabel('Number of Records')
    plt.title(str(x) + ' - Frequence Binning')

    # Save the plot to a buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)

    # Encode the image in base64 and log it
    img_base64 = base64.b64encode(buf.read()).decode('utf-8')

    # Save the plot as a file
    output_filename = '../output/Binning_Frequency_' + str(x)
    plt.savefig(output_filename)
    logger.info("Binning plot saved as" + str(output_filename))

    # Close the buffer
    buf.close()
    plt.close()



plot_distance_bins('Age')
plot_frequency_bins('Age')

# plot_distance_bins('HeartRate')
# plot_frequency_bins('HeartRate')

# plot_distance_bins('BloodSugar')
# plot_frequency_bins('BloodSugar')