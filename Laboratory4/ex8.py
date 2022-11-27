import os


def get_all_files_absolute_paths(dir_path):
    list_of_files = []
    for (root, dirs, files) in os.walk(dir_path):
        for file_name in files:
            list_of_files.append(os.path.abspath(file_name))
    return list_of_files
