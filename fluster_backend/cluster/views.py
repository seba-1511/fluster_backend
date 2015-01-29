import json
from dropbox.client import DropboxClient
from django.http import HttpResponse
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from time import sleep


def get_files(client):
    directory = client.metadata('/')
    return zip(*[client.get_file_and_metadata(f['path'])
                 for f in directory['contents']])


def cluster_files(files, metadata):
    km = KMeans(n_clusters=2, init='k-means++')
    vectorizer = CountVectorizer(input='content', analyzer='word',
                                 max_features=200, stop_words='english',
                                 encoding='utf16')
    print 'Vectorizing files'
    X = vectorizer.fit_transform(files)
    print 'Fitting'
    km.fit(X)
    cluster = [[], []]
    print 'Clustering'
    for f, data in zip(files, metadata):
        cluster[km.predict(f)].append(data.path)
    return cluster


def launch_clustering(request, token):
    print 'Getting Client'
    client = DropboxClient(token)
    print 'Downloading the files'
    # files, metadata = get_files(client)
    # files = [f.read() for f in files]
    print 'Clustering init...'
    cluster = client.metadata('/')
    # cluster = cluster_files(files, metadata)
    # Simulate upload work:
    sleep(3.0)
    return HttpResponse(json.dumps(cluster))
