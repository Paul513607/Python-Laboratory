import os


def write_filepaths_that_start_with_A(director, filepath):
    try:
        file_desc = open(filepath, 'w')
        for file in os.listdir(director):
            if file[0] == 'A' or file[0] == 'a':
                file_desc.write(os.path.abspath(file) + '\n')
        file_desc.close()
    except IOError:
        print('Error: File not found.')
