import os


def file_paths_in_dir(path):
    """List file paths found in 'path'."""
    file_paths = []
    for root, dir, files in os.walk(path):
        for file in files:
            file_paths.append(os.path.join(root, file))
    return file_paths


def get_files(file_paths):
    """Open all files in file paths."""
    for file_path in file_paths:
        with open(file_path) as f:
            yield f


def put_files(folder_paths, files):
    print folder_paths
