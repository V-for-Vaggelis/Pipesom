def read_data(filepath, replace_nan, scale):
    """ Reads a csv file

    INPUT: filepath -> The file's relative path
           replace_nan -> type=boolean -> Wheter or not to replace the nan values
           scale -> type = boolean -> Whether or not to scale the data

    OUTPUT: feature_names = names of the variables
            X -> 2D array with all the data
            droped_features = array with names of variables dropped before training
    """

    import numpy as np
    import pandas as pd
    from sklearn.preprocessing import MinMaxScaler, scale, StandardScaler, normalize
    import warnings

    data = pd.read_csv(filepath)
    feature_names = list(data.columns.values) #the headers
    X = data[feature_names].values #the data

    # clear the data of nan
    droped_features = []
    if replace_nan:

        del_indices = []
        for i,variable in enumerate(X.T):

            if np.isnan(variable).sum()/len(variable) >= 0.7: # if more than 50% is naN drop the feature

                droped_features.append(feature_names[i])
                del_indices.append(i)

                continue

        feature_names = [name for j, name in enumerate(feature_names) if j not in del_indices] #keep non-deleted names
        X = np.delete(X,del_indices,1) #by passing a list we can delete multiple columns of an an np array
        X = X[~np.isnan(X).any(axis=1)] # clear all rows with at least one nan

    if __name__ == "__main__":
        print("Clean data dimensions: {}".format(X.shape))


    def nans_to_mean(data):
        """ Replaces all naNs with the mean value

        INPUT: data -> An array containing naNs

        OUTPUT: The array with it's mean value instead of naNs
        """

        mean = np.nanmean(data)
        inds = np.where(np.isnan(data))
        data[inds] = mean
        return data


    # scale the data to avoid problems in training
    if scale:
        scaler = StandardScaler()
        scaler.fit(X)
        X = scaler.transform(X)

    return feature_names, X, droped_features




if __name__ == "__main__":
    # for debugging
    import numpy as np

    # headers, clear_X, droped = read_data("Agias-Sofias_2018.csv", True, True)
    headers, clear_X, droped = read_data("Auth_2018.csv", True, True)


    print(headers)
    print(len(clear_X[:,0])) # this will be a training point
    print("Dropped features: {}".format(droped))

    count = 0
    for i,data in enumerate(clear_X):
        for j,x in enumerate(data):
            x = float(x)
            if not np.isfinite(x):
                # print(i,j,x)
                count += 1
    print("\n{} naNs in the data".format(count))
