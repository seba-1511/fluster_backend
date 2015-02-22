from abc import abstractmethod
import numpy as np


#: How to integrate multiple cluster configurations?
#: this won't scale for hierarchies so it might not even be worth trying.


class NClusters():

    @abstractmethod
    def fit(self, X):
        """Fit the model to the data."""

    @abstractmethod
    def predict(self, X):
        """Predict the number of clusters."""

    def fit_predict(self, X):
        return self.fit(X).predict(X)

class RootN(NClusters):
    """This is a common heuristic to guess the number of clusters."""

    #: find reference

    def fit(self, X):
        return self

    def predict(self, X):
        return int(np.sqrt(X.shape[0] / 2))