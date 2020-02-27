def analyze_som(labels, data):
    """ Performs SOM train on a dataset

    INPUTS: labels = names of the variables
            data = values of the variables

    OUTPUTS: bytes_image = A multiple-plot of the feature planes as a byte object, can be used directly by an API
    """

    import numpy as np
    import matplotlib.pyplot as plt
    from minisom import MiniSom
    import io

    # train the network
    # TODO: maybe allow the user to request more complex parameters for the network
    size = 15
    som = MiniSom(size, size, len(data[0]),
                  neighborhood_function='gaussian', sigma=1.5,
                  random_seed=1)

    som.pca_weights_init(data)
    som.train_random(data, 1000, verbose=True)

    # create a plane as subplot for each variable
    W = som.get_weights()
    feat_num = len(data[0])
    rows = feat_num//3 if feat_num%3 == 0 else feat_num//3 + 1

    plt.figure(figsize=(10, 10))
    for i, f in enumerate(labels):
        plt.subplot(rows, 3, i+1)
        plt.title(f)
        plt.pcolor(W[:,:,i].T, cmap='coolwarm')
        plt.colorbar()
        plt.xticks(np.arange(size+1))
        plt.yticks(np.arange(size+1))
    plt.tight_layout()

    # will save the image so it can be used directly by flask API
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png', bbox_inches='tight')
    bytes_image.seek(0)
    # plt.savefig("planes.png", bbox_inches='tight')

    if __name__ == "__main__":
        plt.show()

    return bytes_image



# for debugging
from data_reader import read_data

headers, clear_X, droped = read_data("Agias-Sofias_2018.csv", True, True)
# headers, clear_X, droped = read_data("Auth_2018.csv", True, True)

analyze_som(headers, clear_X)
