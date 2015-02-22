import unittest

from fluster_cluster.datasets.real_dropbox import gabrielpereyra
from fluster_cluster.pipeline.base import organize

from fluster_cluster.utils.file import file_paths_in_dir, get_files, put_files
from fluster_cluster.feature_extraction import TfidfVectorizer
from fluster_cluster.cluster import KMeans
from fluster_cluster.cluster_name.base import LabelNames
from fluster_cluster.cluster_size.base import RootN

extract = TfidfVectorizer()
size = RootN()
cluster = KMeans()
name = LabelNames()


#: integration testing? Test production config?

#: how to test the different clustering algorithms?
#: how does sklearn do it?

#: test for sklearn hierarchical clustering

class TestPipeline(unittest.TestCase):

    def test_default_pipeline(self):
        file_paths = file_paths_in_dir(gabrielpereyra.__path__[0])
        files = get_files(file_paths)
        folder_paths = organize(files, extract, size, cluster, name)
        put_files(folder_paths, files)