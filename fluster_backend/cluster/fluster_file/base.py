from dropbox.client import DropboxClient


def get_files_and_contents(token):
    """
    Returns a list of dictionaries that have filenames as keys
    and the respective file contents, as a string, as values.
    """
    client = DropboxClient(token)
    file_paths = get_file_paths(client)
    file_contents = get_file_contents(file_paths, client.metadata)

    files_and_contents = []

    for file_path, file_content in zip(file_paths, file_contents):
        files_and_contents.append(file_path, file_content)

    return files_and_contents


def get_file_paths(client, path='/'):
    """
    Recursively get all file paths starting from 'path'.
    """
    contents = client.metadata(path)['contents']
    folder_paths = [file['path'] for file in contents if file['is_dir']]
    file_paths = [file['path'] for file in contents if not file[
        'is_dir'] and file['mime_type'] == 'text/plain']

    for folder_path in folder_paths:
        file_paths += get_file_paths(folder_path)

    return file_paths


def get_file_contents(file_paths, metadata_list):
    """
    Parse the files to get contents.
    """
    file_contents = []
    for file_path, metadata in zip(file_paths, metadata_list):
        file_contents.append(parse(file_path, metadata))
