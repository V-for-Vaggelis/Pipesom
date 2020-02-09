def read_data(filepath, replace_nan, scale):
    """ Reads a csv file

    INPUT: filepath -> The file's relative path
           replace_nan -> type=boolean -> Wheter or not to replace the nan values
           scale -> type = boolean -> Whether or not to scale the data

    OUTPUT: feature_names = names of the variables
            X -> 2D array with all the data
    """

    import numpy as np
    import pandas as pd
    from sklearn.preprocessing import MinMaxScaler, scale, StandardScaler, normalize
    import warnings

    data = pd.read_csv(filepath)
    feature_names = list(data.columns.values) #the headers
    X = data[feature_names].values #the data

    def nans_to_mean(data):
        """ Replaces all naNs with the mean value

        INPUT: data -> An array containing naNs

        OUTPUT: The array with it's mean value instead of naNs
        """

        mean = np.nanmean(data)
        inds = np.where(np.isnan(data))
        data[inds] = mean
        return data

    def nans_to_zero(data):
        """ Replaces all naNs with zero

        INPUT: data -> An array containing naNs

        OUTPUT: The array with zero instead of naNs
        """

        inds = np.where(np.isnan(data))
        data[inds] = 0
        return data

    # clear the data of naNs
    if replace_nan:
        for i,feature in enumerate(X.T):

            if not np.isfinite(feature).any(): #if all values are naNs drop it cause it creates problems
                if __name__ == "__main__":
                    print("Dropping variable: {}".format(feature_names[i]))
                del feature_names[i]
                continue
            if not np.isfinite(feature).all():
                new_feature = nans_to_mean(feature)
                X[:,i] = new_feature

    # scale the data to avoid problems in training
    if scale:
        scaler = MinMaxScaler((-1,1))
        scaler.fit(X)
        X = scaler.transform(X)

    return feature_names, X





# for debugging
if __name__ == "__main__":
    import numpy as np

    headers, clear_X = read_data("Agias-Sofias_2018.csv", True, True)
    print(headers)
    print(clear_X[:,0]) # this will be a training point

    count = 0
    for i,data in enumerate(clear_X):
        for j,x in enumerate(data):
            x = float(x)
            if not np.isfinite(x):
                print(i,j,x)
                count += 1
    print("\n{} naNs in the data".format(count))
