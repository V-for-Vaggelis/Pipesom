# source = https://datatofish.com/correlation-matrix-pandas/
def corr_mat(labels, values):
    """ Creates a correlation tabulate

    INPUTS: labels -> A list holding the names of the variables
            values -> A list holding the values of each variables

    OUTPUT: bytes_image = A byte-object image of the correlation matrix, can be used directly by an API
    """

    from pandas import DataFrame
    import seaborn as sn
    import matplotlib.pyplot as plt
    import numpy as np
    import io

    Data = dict(zip(labels, values.T)) #creates a dictionary in one line
    # print(Data)

    df = DataFrame(Data, columns=labels)

    corrMatrix = df.corr()
    sn.heatmap(corrMatrix, annot=True)
    plt.tight_layout()

    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png', bbox_inches='tight')
    bytes_image.seek(0)

    if __name__ == "__main__":
        plt.show()

    return bytes_image



# for-debugging
from data_reader import read_data

# headers, clear_X = read_data("Agias-Sofias_2018.csv", False, False)
headers, clear_X, _ = read_data("Auth_2018.csv", False, False)
img = corr_mat(headers, clear_X)
