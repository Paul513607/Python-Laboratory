import os
import sys


def list_unique_extensions():
    if len(sys.argv) < 2:
        raise Exception('No argument provided.')
    if not os.path.isdir(sys.argv[1]):
        raise Exception('Path provided is not a directory.')
    extensions = set()
    for file in os.listdir(sys.argv[1]):
        if file.find('.') > 0:
            extension = file[file.find('.') + 1:]
            extensions.add(extension)
    return extensions
