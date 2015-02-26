import fluster
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans


def pipeline(token):
    """
    Call this to get files from dropbox, parse, cluster,
    and return cluster results.

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
    print 'getting client...'
    db = fluster.DropboxFluster(token)
    print 'getting file paths...'
    paths = db.get_file_paths()
    print 'downloading files...'
    db.get_files_and_write(paths)
    print 'parsing files...'
    contents = db.parse_files_in_folder('dropbox_files/')

    print 'fitting and clustering...'
    X = TfidfVectorizer().fit_transform(contents)
    km = KMeans(n_clusters=4)
    X = km.fit_transform(X)
    labels = km.labels_
    return X, labels
