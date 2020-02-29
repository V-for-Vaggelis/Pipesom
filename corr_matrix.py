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
    import time

    # get current_time to use as file name extension, this will help in caching
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    time = current_time.replace(":", "-")

    Data = dict(zip(labels, values.T)) #creates a dictionary in one line
    # print(Data)

    df = DataFrame(Data, columns=labels)

    corrMatrix = df.corr()
    sn.heatmap(corrMatrix, annot=True)
    plt.tight_layout()

    # bytes_image = io.BytesIO()
    # plt.savefig(bytes_image, format='png', bbox_inches='tight')
    # bytes_image.seek(0)
    plt.savefig("static/corr-{}.png".format(time), bbox_inches='tight')

    if __name__ == "__main__":
        plt.show()

    plt.close("all")
    # return bytes_image


if __name__ == "__main__":
    # for-debugging
    from data_reader import read_data

    # headers, clear_X = read_data("Agias-Sofias_2018.csv", False, False)
    headers, clear_X, _ = read_data("Auth_2018.csv", False, False)
    corr_mat(headers, clear_X)
