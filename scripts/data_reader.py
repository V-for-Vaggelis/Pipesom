def read_data(filepath):

    import numpy as np
    import pandas as pd
    from sklearn.preprocessing import minmax_scale, scale
    import warnings

    data = pd.read_csv(filepath)
    feature_names = list(data.columns.values) #the headers
    X = data[feature_names].values #the data
    X = scale(X) #normalizing

    def nans_to_mean(data):
        """ Replaces all naNs with the mean value

        INPUT: An array containing naNs

        OUTPUT: The array with it's mean value instead of naNs
        """

        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=RuntimeWarning)
            mean = np.nanmean(data)
        inds = np.where(np.isnan(data))
        data[inds] = mean
        return data

    def nans_to_zero(data):
        """ Replaces all naNs with zero

        INPUT: An array containing naNs

        OUTPUT: The array with zero instead of naNs
        """

        inds = np.where(np.isnan(data))
        data[inds] = 0
        return data

    # clear the data of naNs
    clear_X = []
    for feature in X:
        ## TODO: Find a way to make meab replacement, or a better interpolation work
        # new_feature = nans_to_mean(feature)
        if not np.isfinite(feature).all():
            new_feature = nans_to_zero(feature)
            clear_X.append(new_feature)
        else:
            clear_X.append(feature)

    return feature_names, clear_X


# for debugging
if __name__ == "__main__":
    import numpy as np

    headers, clear_X = read_data("Agias-Sofias_2018.csv")
    print(headers)
    print(clear_X)

    count = 0
    for i,data in enumerate(clear_X):
        for j,x in enumerate(data):
            x = float(x)
            if not np.isfinite(x):
                print(i,j,x)
                count += 1
    print("\n{} naNs in the data".format(count))
