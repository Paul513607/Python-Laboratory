import os


def get_dict_for_file(filepath):
    return {
        "full_path": os.path.abspath(filepath),
        "file_extension": filepath.split('.')[-1],
        "can_read": os.access(filepath, os.R_OK),
        "can_write": os.access(filepath, os.W_OK)
    }
