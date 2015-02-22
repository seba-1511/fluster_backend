from ..utils.parse import parse


def organize(files, extract, size, cluster, name):
    """Create new file structure.

    :param files:
    :param extract:
    :param cluster:
    :param name:

    :returns: a list of new file paths.
    """
    contents = parse(files)
    X = extract.fit_transform(contents).toarray()
    cluster.n_clusters = size.fit_predict(X)
    L = cluster.fit_predict(X)
    name.fit(X, extract, cluster)
    return name.predict(L)


def structured_organize():
    """Learn existing file structure.

    :param files:
    :param extract:
    :param cluster:
    :param name:

    :returns: a list of new file paths.
    """
    raise NotImplementedError
