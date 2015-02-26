import fluster
# from dropbox
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans


def pipeline(token):
    """
    Call this to get files from dropbox, parse, cluster and return cluster results.

    Parameters
    ----------
    token : Dropbox API token

    Return Values
    -------------
    X : array-like, shape (n_samples, 2)
        2D coordinates of resulting clusters

    labels : array-like, shape (n_samples, )
        Cluster assignments

    """

    db = fluster.Fluster(token)
    paths = db.get_file_paths()
    db.get_files_and_write(paths)
    contents = db.parse_files_in_folder('dropbox_files/')

    X = TfidfVectorizer().fit_transform(contents)
    km = KMeans(n_clusters=2)
    X = km.fit_transform(X)
    labels = km.labels_
    return X, labels
