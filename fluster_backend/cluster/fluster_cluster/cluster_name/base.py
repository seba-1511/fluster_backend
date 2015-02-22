

class Namer():

    def predict(self, L):
        return [self.label_to_name[label] for label in L]


#: Initially these should all work with sklearn's kmeans implementation.
#: how do we extend them to work with other models?

#: These also suggest that the two layer kmeans label scheme should be
#: something like [1/2] representing the first layer label and second layer
#: label within the group of files in the first cluster.


class LabelNames(Namer):
    """Converts label id to a string to use as folder name."""

    #: how do we extend this to two layer kmeans?

    def fit(self, X, extract, cluster):
        """Place holder for namers. Maps labels to labels"""
        labels = cluster.labels_
        names = [str(label) for label in labels]
        self.label_to_name = dict(zip(labels, names))
        return self


class MostCommonWord(Namer):
    """Converts label id to most common word in cluster."""

    def fit(self, X, extract, cluster):
        raise NotImplementedError


class MostCommonWords(Namer):
    """Converts label id to 'n' most common words in cluster."""

    def __init__(self, n):
        self.n = n

    def fit(self, X, extract, cluster):
        raise NotImplementedError


class NGram(Namer):
    """Converts label id to most common phrase of length 'n' in cluster."""

    def __init__(self, n):
        self.n = n

    def fit(self):
        raise NotImplementedError