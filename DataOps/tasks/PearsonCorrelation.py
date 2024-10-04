import pandas as pd
from scipy.stats import pearsonr
import logging
from matplotlib import pyplot as plt
import io
import base64
from tabulate import tabulate


# Configure standard Python logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Import the data
df = pd.read_csv("../data/MedicalDatasetForModelNormalized.csv")
logger.info("Dataset loaded for Pearson correlation.")

# store results
result_data = []

def compute_pearson_correlation(x, y):    
    # Convert columns to series
    list1 = df[x]
    list2 = df[y]

    # Compute Pearson correlation
    corr, _ = pearsonr(list1, list2)
    logger.info(f'Pearson correlation between {x} and {y}: {corr:.3f}')

    # Scatter plot
    plt.scatter(list1, list2)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title('Scatter plot of ' + str(x) + ' vs ' + str(y))

    # Save the plot to a buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)

    # Encode the image in base64 and log it
    img_base64 = base64.b64encode(buf.read()).decode('utf-8')

    # Save the plot as a file
    output_filename = '../output/' + str(x) + '_' + str(y)
    plt.savefig(output_filename)
    logger.info("Scatter plot saved as" + str(output_filename))

    # Close the buffer
    buf.close()
    plt.close()
    result_data.append([x, y, corr])

compute_pearson_correlation('Age', 'HeartRate')
compute_pearson_correlation('Age', 'BloodSugar')
compute_pearson_correlation('Age', 'Troponin')
compute_pearson_correlation('Age', 'CKMB')
compute_pearson_correlation('BloodSugar', 'Troponin')
compute_pearson_correlation('SystolicBloodPressure', 'Troponin')
compute_pearson_correlation('DiastolicBloodPressure', 'Troponin')
compute_pearson_correlation('Age', 'Result')
compute_pearson_correlation('BloodSugar', 'Result')
compute_pearson_correlation('CKMB', 'Result')
compute_pearson_correlation('Troponin', 'Result')

headers = ["Variable1", "Variable2", "PearsonCorrelation"]
print(tabulate(result_data, headers = headers, tablefmt = "fancy_grid"))