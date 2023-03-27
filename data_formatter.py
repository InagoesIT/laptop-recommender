import os
import re
import pandas as pd


class DataFormatter:
    def __init__(self, files_dir):
        self.files_dir = files_dir

    def rename_files(self):
        pattern = r'(The_Best_)(.+)(_for|_in)'
        for root, dir_names, file_names in os.walk(self.files_dir):
            for file_name in file_names:
                new_file_name = re.findall(pattern, file_name)[0][1]
                os.rename(os.path.join(root, file_name), os.path.join(root, new_file_name))

    def add_csv_ending(self):
        for root, dir_names, file_names in os.walk(self.files_dir):
            for file_name in file_names:
                full_file_name = os.path.join(root, file_name)
                os.rename(full_file_name, f"{full_file_name}.csv")

    def reformat_files(self):
        for root, dir_names, file_names in os.walk(self.files_dir):
            for file_name in file_names:
                full_file_name = os.path.join(root, file_name)
                data_frame = pd.read_csv(full_file_name)
                data_frame.drop('Source Url', axis=1, inplace=True)
                data_frame.drop('Url', axis=1, inplace=True)
                data_frame.to_csv(full_file_name)


if __name__ == '__main__':
    dataFormatter = DataFormatter('resources')
    dataFormatter.reformat_files()

