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

    def delete_first_2_columns(self):
        for root, dir_names, file_names in os.walk(self.files_dir):
            for file_name in file_names:
                full_file_name = os.path.join(root, file_name)
                df = pd.read_csv(full_file_name)
                # df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
                df.drop('Source Url', axis=1, inplace=True)
                df.drop('Url', axis=1, inplace=True)
                df.to_csv(full_file_name)

    def delete_first_3_rows(self):
        #"2-in-1_Laptops.csv", "Battery_Life_Laptops.csv", "Business_Laptops.csv",
        # "Laptops_for_College_Students.csv", "Laptops_for_Video_Editing.csv"
        files_to_delete_from = ["Business_Laptops.csv"]
        for root, dir_names, file_names in os.walk(self.files_dir):
            for file_name in file_names:
                if file_name not in files_to_delete_from:
                    continue
                full_file_name = os.path.join(root, file_name)
                df = pd.read_csv(full_file_name)
                df.drop(index=[0, 1, 2], inplace=True)
                df.to_csv(full_file_name)


if __name__ == '__main__':
    dataFormatter = DataFormatter('resources')
    dataFormatter.delete_first_2_columns()

