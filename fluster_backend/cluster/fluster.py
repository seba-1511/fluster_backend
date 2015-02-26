import dropbox
from parse import parse
import os


class DropboxFluster:

    """ Will retrieve and parse files in given dropbox. """

    def __init__(self, token):
        self.client = dropbox.client.DropboxClient(token)

    def parse_files_in_folder(self, folder):
        """ Will parse all files within given folder and
        return file names and contents. """
        file_paths = os.listdir(folder)
        return [parse('dropbox_files/' + path) for path in sorted(file_paths)]

    def get_file_paths(self, path='/'):
        """ Recursively get all file paths starting from 'path'. """
        contents = self.client.metadata(path)['contents']
        folder_paths = [file['path'] for file in contents if file['is_dir']]
        file_paths = [file['path'] for file in contents if not file[
            'is_dir']]

        for folder_path in folder_paths:
            file_paths += self.get_file_paths(folder_path)

        return sorted(file_paths)

    def get_files_and_write(self, paths):
        """ Opens and returns file objects. """
        for path in paths:
            dropbox_file = self.client.get_file(path)
            contents = dropbox_file.read()
            file_name = 'dropbox_files/' + os.path.basename(path)
            with open(file_name, 'wb') as f:
                f.write(contents)
