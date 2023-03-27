import os
import re


class DataFormatter:
    def __init__(self, files_dir):
        self.files_dir = files_dir

    def rename_files(self):
        pattern = r'(The_Best_)(.+)(_for|_in)'
        for root, dir_names, file_names in os.walk(self.files_dir):
            for file_name in file_names:
                new_file_name = re.findall(pattern, file_name)[0][1]
                os.rename(os.path.join(root, file_name), os.path.join(root, new_file_name))


if __name__ == '__main__':
    data = DataFormatter('resources')

