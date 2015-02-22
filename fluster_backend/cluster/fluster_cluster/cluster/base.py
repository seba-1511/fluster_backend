from abc import abstractmethod


class Clusterer():
    """Defines sklearn interface."""

    @abstractmethod
    def fit(self, X):
        """Fit the model to the data."""

    @abstractmethod
    def predict(self, X):
        """Predict cluster labels."""

    def fit_predict(self, X):
        """Fit method should return self for this to work."""
        return self.fit(X).predict(X)


class TwoLayerKmeans(Clusterer):
    def __init__(self, n_clusters, cluster_size):
        """

        :param n_clusters: number of clusters in first layer.
        :param cluster_size: how to predict number of clusters in second layer.
        """
        self.n_clusters = n_clusters
        self.cluster_size = cluster_size

    def predict(self, X):
        """Predict cluster labels."""

        #: I think the way we want to encode cluster labels is an numpy array
        #: with shape (n, 2) where labels[i][0] represents the first layer
        #: cluster of the ith example and labels[i][1] represents the second
        #: layer cluster of the ith example.

    def fit_predict(self, X):
        """Predict cluster labels."""

        #: run sklearn fit to get first layer cluster assignments.
        #: for each cluster
        #:     predict number of second layer clusters in first layer cluster.
        #:     update kmeans n_cluster attribute
        #:     run fit to get second layer cluster assignments
        #: return a numpy array as described in predict