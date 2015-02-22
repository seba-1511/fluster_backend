import json
from dropbox.client import DropboxClient
from django.http import HttpResponse
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from fluster_cluster.fluster_cluster.pipeline.base import organize
from fluster_cluster.fluster_cluster.cluster_name.base import LabelNames
from fluster_cluster.fluster_cluster.cluster_size.base import RootN


def get_files(client):
    directory = client.metadata('/')
    return zip(*[client.get_file_and_metadata(f['path'])
                 for f in directory['contents']])


def launch_clustering(request, token):
    extract = TfidfVectorizer()
    size = RootN()
    cluster = KMeans()
    name = LabelNames()
    client = DropboxClient(token)
    files = get_files(client)  # Returns the files and metadata
    folder_paths = organize(files, extract, size, cluster, name)
    return HttpResponse(json.dumps(folder_paths))
