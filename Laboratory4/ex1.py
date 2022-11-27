import os


def list_extensions(director):
    extensions = []
    for file in os.listdir(director):
        if file.find('.') > 0:
            extensions.append(file.split('.')[-1])
    extensions.sort()
    return extensions
